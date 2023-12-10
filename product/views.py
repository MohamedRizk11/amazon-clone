from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product,Productimage, Brand ,Review
# Create your views here.


class Productliist(ListView):
    model = Product



class ProductDetail(DetailView):
    model = Product    