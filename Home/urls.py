from django.urls import path
from . import views


app_name = 'Home'
urlpatterns = [
    path('', views.indexview.as_view(), name='indexview'),
    path('<int:pk>/', views.SpecificProduct.as_view(), name='Specific_Product'),
    path('cart/', views.cart.as_view(), name='cart'),
]