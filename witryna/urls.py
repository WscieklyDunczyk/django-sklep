from django.urls import path
from . import views
from .views import (
    ProduktListView,
    ProduktDetailView,
    ProduktCreateView,
    ProduktUpdateView,
    ProduktDeleteView,
)

# int w <int:pk> mówi o tym, że spodziewamy się tylko wartości liczbowych w tym miejscu
# ProduktUpdateView i ProduktCreateView korzystają z tego samego szablonu html
urlpatterns = [
    path('', ProduktListView.as_view(), name="witryna-home"),
    path('produkt/<int:pk>/', ProduktDetailView.as_view(), name='produkt-detail'),
    path('produkt/new/', ProduktCreateView.as_view(), name='produkt-create'),
    path('produkt/<int:pk>/update/', ProduktUpdateView.as_view(), name='produkt-update'),
    path('produkt/<int:pk>/delete/', ProduktDeleteView.as_view(), name='produkt-delete'),
    path('contact/', views.contact, name="witryna-contact"),
    path('search/', views.search, name="witryna-search"),
]
