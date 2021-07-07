from django.urls import path
from . import views


app_name = 'Home'
urlpatterns = [
    path('', views.indexview.as_view(), name='indexview'),
]