from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
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



class SpecificProduct(DetailView):

    model = Product
    template_name = 'Home/specificProduct.html'
    context_object_name = 'productinfo'

    def get(self, request, *args, **kwargs):
        id =  self.kwargs.get('pk')
        product_info = self.model.objects.get(pk=id)

        return render(request, self.template_name, {self.context_object_name: product_info})
    

