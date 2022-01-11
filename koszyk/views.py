from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from witryna.views import Produkt
from .models import Cart, Order
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)


@login_required
def cart(request):
    user = request.user
    koszyk = Cart.objects.filter(user=user)

    # obliczenie wartości wszystkich koszykow dla danego użytkownika
    suma = 0
    for item in koszyk:
        suma += item.total_price()

    context = {
        'cart_products': koszyk,
        'suma_zamowienia': suma,
    }
    return render(request, 'koszyk/cart.html', context)


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Produkt, id=product_id)

    item_in_cart = Cart.objects.filter(product=product_id, user=user)
    if item_in_cart:
        cart_item = get_object_or_404(Cart, product=product_id, user=user)
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart(user=user, product=product).save()
    return redirect('cart')


@login_required
def plus_item(request):
    item_id = request.GET.get('item_id_plus')
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=item_id)
        cp.quantity += 1
        cp.save()
    return redirect('cart')


@login_required
def minus_item(request):
    item_id = request.GET.get('item_id_minus')
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=item_id)
        if cp.quantity == 1:
            cp.delete()
        else:
            cp.quantity -= 1
            cp.save()
    return redirect('cart')


@login_required
def order(request):
    user = request.user
    carts = Cart.objects.filter(user=user)

    for c in carts:
        Order(user=user, product=c.product, quantity=c.quantity).save()

        c.delete()
    messages.success(request, f'Zamówienie zostało złożone do realizacji!')
    return redirect('witryna-home')
