from django.shortcuts import render
from django.views import View

from .models import CategoryModel, CarModel

from .forms import BookingForm, ContactForm
from .models import CategoryModel, CarouselImage, ContactModel

class HomeView(View):
    def get(self, request):
        category_list = CategoryModel.objects.all()
        booking_form = BookingForm()
        contact_form = ContactForm()  # Initialize the Contact form
        carousel_images = CarouselImage.objects.all()  # Fetch all carousel images
        
        context = {
            'category_list': category_list,
            'booking_form': booking_form,
            'contact_form': contact_form,  # Add the Contact form to context
            'carousel_images': carousel_images,
        }
        
        return render(request, 'home.html', context=context)

    def post(self, request):
        category_list = CategoryModel.objects.all()
        booking_form = BookingForm(request.POST)
        contact_form = ContactForm(request.POST)  # Handle contact form submission
        
        if 'booking_form' in request.POST:
            # Handle booking form submission
            if booking_form.is_valid():
                booking_form.save()
                message = 'Booking successfully submitted!'
            else:
                message = 'There was an error in your booking submission.'
        
        elif 'contact_form' in request.POST:
            # Handle contact form submission
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
            'carousel_images': CarouselImage.objects.all(),  # Pass carousel images
        }
        
        return render(request, 'home.html', context=context)


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    

class ContactView(View):
    def get(self, request):
        contact_form = ContactForm()  # Create a new form instance
        return render(request, 'contact.html', {'contact_form': contact_form})

    def post(self, request):
        contact_form = ContactForm(request.POST)  # Pass POST data to the form
        
        if contact_form.is_valid():  # If the form is valid, save the data
            contact_form.save()  # Save the form data to the database
            message = 'Your message has been successfully submitted.'
        else:
            message = 'There was an error in your submission. Please try again.'
        
        # Render the contact page again with the form and the message
        return render(request, 'contact.html', {
            'contact_form': contact_form,
            'message': message
        })
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

