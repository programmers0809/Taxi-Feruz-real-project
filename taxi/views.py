from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from .models import CategoryModel, CarModel, CarouselImage, Service
from .forms import BookingForm, ContactForm


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        category_list = CategoryModel.objects.all()
        booking_form = BookingForm()
        contact_form = ContactForm()
        carousel_images = CarouselImage.objects.all()
        
        context = {
            'category_list': category_list,
            'booking_form': booking_form,
            'contact_form': contact_form,
            'carousel_images': carousel_images,
        }
        
        return render(request, 'home.html', context=context)

    def post(self, request):
        category_list = CategoryModel.objects.all()
        booking_form = BookingForm(request.POST)
        contact_form = ContactForm(request.POST)
        
        if 'booking_form' in request.POST:
            if booking_form.is_valid():
                booking_form.save()
                message = 'Booking successfully submitted!'
            else:
                message = 'There was an error in your booking submission.'
        
        elif 'contact_form' in request.POST:
            if contact_form.is_valid():
                contact_form.save()
                message = 'Contact form successfully submitted!'
            else:
                message = 'There was an error in your contact form submission.'
        
        context = {
            'category_list': category_list,
            'booking_form': booking_form,
            'contact_form': contact_form,
            'message': message,
            'carousel_images': CarouselImage.objects.all(),
        }
        
        return render(request, 'home.html', context=context)


class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'about.html')
    

class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        contact_form = ContactForm()
        return render(request, 'contact.html', {'contact_form': contact_form})

    def post(self, request):
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            message = 'Your message has been successfully submitted.'
        else:
            message = 'There was an error in your submission. Please try again.'
        
        return render(request, 'contact.html', {
            'contact_form': contact_form,
            'message': message
        })


class ServicesView(LoginRequiredMixin, View):
    def get(self, request):
        services = Service.objects.all()
        return render(request, 'service.html', {'services': services})


class CarsView(LoginRequiredMixin, View):
    def get(self, request):
        economic_list = CarModel.objects.filter(category__name="Ekanomik").order_by('-publish_time')[:3]
        standart_list = CarModel.objects.filter(category__name="Standart").order_by('-publish_time')[:3]
        lux_list = CarModel.objects.filter(category__name="Lyuks").order_by('-publish_time')[:3]

        context = {
            'economic_list': economic_list,
            'standart_list': standart_list,
            'lux_list': lux_list,
        }

        return render(request, 'cars.html', context=context)


def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')  # Logoutdan keyin xabar
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')  # Redirect to home page
        else:
            messages.error(request, 'Login or password is incorrect!')
    return render(request, 'login.html')
        

class WelcomeView(View):
    def get(self, request):
        return render(request, 'welcometosait.html')
