from django.urls import path
from .views import cart, add_to_cart, plus_item, minus_item, order

urlpatterns = [
    path('cart/', cart, name="cart"),
    path('cart/add-to-cart', add_to_cart, name="add-to-cart"),
    path('cart/plus-item', plus_item, name="plus-item"),
    path('cart/minus-item', minus_item, name="minus-item"),
    path('cart/order', order, name="order"),
]
