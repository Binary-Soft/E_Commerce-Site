from django.shortcuts import render
from django.views import View
from .models import Head_Offer_Photo_Section, Product

# Create your views here.

class indexview(View):
    
    model1 = Head_Offer_Photo_Section
    model2 = Product
    template_name = 'Home/index.html'
    context_object_name1 = 'AllOffers'
    context_object_name2 = 'ProductsInfo'

    def get(self, request, *args, **kwargs):
        a = self.model1.objects.all()
        b = self.model2.objects.all()
        return render(request, self.template_name, {self.context_object_name1 : a, self.context_object_name2 : b})
