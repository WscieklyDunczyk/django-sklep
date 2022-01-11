from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('witryna.urls')),
                  path('', include('koszyk.urls')),
                  path('register/', user_views.register, name='register'),
                  path('profil/', user_views.profil, name='profil'),
                  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
