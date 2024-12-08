from django.contrib import admin

from .models import CategoryModel, CarModel, BookingModel,CarouselImage,ContactModel,Service

admin.site.register([CategoryModel, CarModel, BookingModel,CarouselImage,ContactModel,Service])


class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'from_location', 'to_location', 'email', 'comfort', 'adults', 'children', 'date', 'time']
    search_fields = ['name', 'email', 'from_location', 'to_location']
    list_filter = ['comfort', 'date']
    ordering = ['-date']
