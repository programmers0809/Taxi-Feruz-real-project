from django.utils import timezone 
from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    image = models.ImageField(upload_to='category_image/', verbose_name='Rasmi')
    
    
    def __str__(self):
        return self.name 
    
    class Meta:
        db_table = 'Category'
        managed = True
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        

class CarModel(models.Model):
    
    image = models.ImageField(upload_to='cars/', verbose_name='Rasmi')
    category = models.ForeignKey(CategoryModel,
                                 verbose_name='Kategoriyasi',
                                 on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now, verbose_name="Mashina qo'shilgan vaqti")
    def __str__(self):
        return self.category.name + ' -'+ self.image.name
    
    class Meta:
        db_table = 'Cars'
        managed = True
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'
        
        
class BookingModel(models.Model):
    COMFORT_CHOICES = [
        ('cheap', 'Ekanom'),
        ('standart', 'Standart'),
        ('lux', 'Lyuks'),
    ]
    
    name = models.CharField(max_length=255)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    email = models.EmailField()
    time = models.TimeField()
    date = models.DateField()
    comfort = models.CharField(max_length=10, choices=COMFORT_CHOICES)
    adults = models.IntegerField()
    children = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f"Taklif keldi {self.name}dan"
    
    class Meta:
        db_table = 'Booking'
        managed = True
        verbose_name = 'Jalb qilish'
        verbose_name_plural = 'Jalb qilishlar'
