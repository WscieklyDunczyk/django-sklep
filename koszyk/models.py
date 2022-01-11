from django.db.models import *
from django.contrib.auth.models import User
from witryna.models import Produkt


class Cart(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    product = ForeignKey(Produkt, on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)
    create_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def total_price(self):
        return self.product.cena * self.quantity

    def __str__(self):
        return f'{self.user.username} - {self.product}'


class Order(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    # adres = ForeignKey(Adres, on_delete=CASCADE, null=True)
    product = ForeignKey(Produkt, on_delete=CASCADE)
    quantity = PositiveIntegerField()
    ordered_date = DateTimeField(auto_now_add=True)
