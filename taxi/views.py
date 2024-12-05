from django.shortcuts import render
from django.views import View

from .models import CategoryModel, CarModel
from .forms import BookingForm

class HomeView(View):
    def get(self, request):
        category_list = CategoryModel.objects.all()

        booking_form = BookingForm()

        context = {
            'category_list': category_list,
            'booking_form': booking_form,
        }
        
        return render(request, 'home.html', context=context)

    def post(self, request):
    
        category_list = CategoryModel.objects.all()
        booking_form = BookingForm(request.POST)
        
        if booking_form.is_valid():
            booking_form.save()
          
            return render(request, 'home.html', {
                'category_list': category_list,
                'booking_form': booking_form,
                'message': 'Booking successfully submitted!'
            })
        
        return render(request, 'home.html', {
            'category_list': category_list,
            'booking_form': booking_form,
            'message': 'There was an error in your booking submission.'
        })
    

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class ServicesView(View):
    def get(self, request):
        return render(request, 'service.html')
    
class CarsView(View):
    def get(self, request):
        
        economic_list = CarModel.objects.all().filter(category__name="Ekanomik").order_by('-publish_time')[:3]
        standart_list = CarModel.objects.all().filter(category__name="Standart").order_by('-publish_time')[:3]
        lux_list = CarModel.objects.all().filter(category__name="Lyuks").order_by('-publish_time')[:3]

        context = {
            'economic_list': economic_list, 
            'standart_list': standart_list,
            'lux_list': lux_list,
        }

        return render(request, 'cars.html', context=context)

