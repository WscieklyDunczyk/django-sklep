from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from django.core.mail import send_mail
from witryna.contact import ContactForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

from .models import Produkt


# Function base views
def home(request):
    context = {
        'produkty': Produkt.objects.all()
    }
    return render(request, 'witryna/home.html', context)


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = request.POST.get('firstname')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            data = {
                'firstname': firstname,
                'surname': surname,
                'email': email,
                'subject': subject,
                'message': message,
            }
            message = '''
                    New message: {}

                    From: {}
                    '''.format(data['message'], data['email'])
            send_mail(data['subject'], message, '', ['djangosklep@gmail.com'])

            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'witryna/contact.html', {'form': form, 'submitted': submitted})


def search(request):
    q = request.GET['q']
    products_list = Produkt.objects.filter(nazwa__icontains=q)
    paginator = Paginator(products_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'witryna/search.html', {'page_obj': page_obj})


# Class base views

# bez wykorzystania konwencji nazewnictwa
class ProduktListView(ListView):
    # zmienna model m??wi, do jakiego modelu b??d?? kierowane zapytania
    model = Produkt
    paginate_by = 8
    # m??wimy gdzie znajduje si?? template dla tego widoku
    # domy??lne ustawienie<nazwa_aplikacji>/<model>_<type_widoku>.html
    template_name = 'witryna/home.html'

    # nazwa, przez kt??r?? odwo??ujemy si?? do listy obiekt??w w szablonie
    # domy??lnie object
    context_object_name = 'produkty'

    # zmiana porz??dku wy??wietlania obiekt??w
    # ustawiony wed??ug zmiennej daty_dodania, - przed nazw?? zmiennej powoduje odwr??cenie kolejno??ci
    ordering = ['-data_dodania']


class ProduktDetailView(DetailView):
    model = Produkt


# LoginRequiredMixin - ??eby dosta?? si?? do widoku na stronie trzeba by?? zalogowanym,
# je??eli nie to przekieruje do widoku logowania
class ProduktCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Produkt

    # ustalenie wymaganych uprawnie?? do wy??wietlenia tego widoku
    permission_required = 'witryna.produkt_add'

    # ustawiamy jakie pola z klasy Produkt maj?? si?? pojawi?? w formularzu podczas tworzenia obiektu
    fields = ['nazwa', 'cena', 'marka', 'opis', 'image']

    # widok, do kt??rego zostanie przekierowana niezalogowana osoba
    login_url = 'login'

    # nadpisujemy funkcje, ??eby do danego widoku dost??p mieli tylko zalogowani u??ytkownicy
    def form_valid(self, form):
        # zanim dane z formularza zostan?? zapisane zostanie dodana do niego zmienna jako obecnie zalogowany u??ytkownik
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ProduktUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Produkt

    # ustalenie wymaganych uprawnie?? do wy??wietlenia tego widoku
    permission_required = 'witryna.produkt_change'

    fields = ['nazwa', 'cena', 'marka', 'opis', 'image']

    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    # test czy zalogowany user to ten sam co doda?? dany produkt
    def test_func(self):
        produkt = self.get_object()
        if self.request.user == produkt.autor:
            return True
        return False


class ProduktDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Produkt

    # przekierowanie na ten adres, kiedy formularz przejdzie pomy??lnie
    success_url = '/'

    # ustalenie wymaganych uprawnie?? do wy??wietlenia tego widoku
    permission_required = 'witryna.produkt_delete'

    def test_func(self):
        produkt = self.get_object()
        if self.request.user == produkt.autor:
            return True
        return False
