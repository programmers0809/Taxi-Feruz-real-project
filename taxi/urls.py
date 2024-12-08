from django.urls import path
from .views import HomeView, CarsView, ContactView, AboutView, ServicesView, WelcomeView
from .views import custom_logout

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome_page'),  # Welcome sahifasi
    path('home/', HomeView.as_view(), name='home_page'),   # Home sahifasi
    path('cars/', CarsView.as_view(), name='cars_page'),   # Cars sahifasi
    path('contact/', ContactView.as_view(), name='contact_page'),  # Contact sahifasi
    path('about/', AboutView.as_view(), name='about_page'),  # About sahifasi
    path('services/', ServicesView.as_view(), name='service_page'),  # Services sahifasi
    path('logout/', custom_logout, name='logout'),  # Logout
]
