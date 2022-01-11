from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profil


# kiedy użytkownik(User) zostanie zapisany(post_save) zostanie wykonana ta funkcja
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # stwórz obiekt Profil z instancją usera, który został przed chwilą utworzony
        Profil.objects.create(user=instance)


# zapisuje Profil kiedy User jest zapisany
@receiver(post_save, sender=User)
def save_profil(sender, instance, **kwargs):
    instance.profil.save()
