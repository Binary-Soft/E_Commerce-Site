from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 10, decimal_places=3, default=0.00)
    description = models.CharField(max_length=200, blank=True)
    warranty = models.DecimalField(max_digits = 10, decimal_places=3, default=0.00)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    weight = models.DecimalField(max_digits = 10, decimal_places=3, default=0.00)
    pic = models.ImageField(upload_to='picture/')

    def __str__(self):
        return self.name
