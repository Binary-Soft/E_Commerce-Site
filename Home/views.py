from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.

class indexview(View):
    
    model = Product
    template_name = 'Home/index.html'
    context_object_name = 'ProductsInfo'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {self.context_object_name : self.model.objects.all()})
