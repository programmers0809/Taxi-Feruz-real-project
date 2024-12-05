from django.urls import path

from .views import HomeView, CarsView, ContactView, AboutView, ServicesView


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('cars/', CarsView.as_view(), name='cars_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('services/', ServicesView.as_view(), name='service_page')
]