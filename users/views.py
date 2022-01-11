from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfilUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto utworzone dla {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profil(request):
    if request.method == 'POST':
        # bez przekazania instancji do funkcji pola na stronie profilu użytkownika będą puste
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Twoje konto zostało zaktualizowane!')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilUpdateForm(instance=request.user.profil)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profil.html', context)
