from django.http.response import HttpResponse, HttpResponseRedirect
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
    context_object_name3 = 'AddCartInfos'

    def get(self, request, *args, **kwargs):
        a = self.model1.objects.all()
        b = self.model2.objects.all()
        
        request.session.clear_expired()
        info = request.session.items()
        print(f'\n\n{info}\n\n')
        li = []
        AddCartInfo = {}
        for (key, value) in info:
            product_info = self.model2.objects.get(pk=int(key))
            li.append(product_info)
            AddCartInfo[product_info] = value
        for product_info in li:
            x = product_info.price
            AddCartInfo[product_info] = {AddCartInfo[product_info]: x*AddCartInfo[product_info]}

        return render(request, self.template_name, {self.context_object_name1 : a,
        self.context_object_name2 : b, self.context_object_name3 : AddCartInfo})
    

    def post(self, request, *args, **kwargs):
        key = request.POST['ID']
        print('\n\nID', key, '\n\n')
        if key in request.session:
            request.session[key] += 1
        else:
            request.session[key] = 1
        return HttpResponseRedirect('/')



class SpecificProduct(DetailView):

    model = Product
    template_name = 'Home/specificProduct.html'
    context_object_name = 'productinfo'

    def get(self, request, *args, **kwargs):
        id =  self.kwargs.get('pk')
        product_info = self.model.objects.get(pk=id)
        return render(request, self.template_name, {self.context_object_name: product_info})
    

class cart(View):
    
    template_name = 'Home/AddCartPage.html'
    context_object_name = 'AddCartInfo'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {self.context_object_name: 'Testing'})
