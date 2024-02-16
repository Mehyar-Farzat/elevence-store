from django.shortcuts import render
from products.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()[:4]
    return render(request,'settings/home.html', {'products':products})
