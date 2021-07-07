from django.contrib import admin
from .models import Head_Offer_Photo_Section, Product

# Register your models here.


class Admin_Head_Offer_Photo_Section(admin.ModelAdmin):
    list_display = ('id', 'picture')

admin.site.register(Head_Offer_Photo_Section, Admin_Head_Offer_Photo_Section)




@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'pic')

