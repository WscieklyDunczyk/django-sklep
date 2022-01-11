from django.db.models import *
from django.contrib.auth.models import User
from PIL import Image


class Adres(Model):
    kraj = CharField(max_length=100)
    miasto = CharField(max_length=100)
    ulica = CharField(max_length=100)
    numer_mieszkania = CharField(max_length=10)


class Profil(Model):
    # jeżeli usuniemy usera profil też zostanie usunięty
    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(default='default.jpg', upload_to='profil_zdjecia')
    adres = OneToOneField(Adres, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profil'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
