from PIL import Image
from django.contrib.auth.models import User
from django.db.models import *
from django.urls import reverse
from django.utils import timezone


class Produkt(Model):
    nazwa = CharField(max_length=100)
    marka = CharField(max_length=100)
    cena = IntegerField()
    opis = TextField()
    # upload_to jest równe nazwie folderu, w którym będą przechowywane obrazy dla tego obiektu
    image = ImageField(default='default.jpg', upload_to='produkt_zdjecia')
    data_dodania = DateTimeField(default=timezone.now)
    autor = ForeignKey(User, on_delete=CASCADE)
    ilosc = IntegerField(default=100)
    dostepny = BooleanField(default=True)

    def __str__(self):
        return self.nazwa

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # po utworzeniu obiektu w formularzu na stronie zostaniemy przekierowani pod adres, który zostanie zwrócony jako
    # string w tej funkcji
    def get_absolute_url(self):
        return reverse('produkt-detail', kwargs={'pk': self.pk})
