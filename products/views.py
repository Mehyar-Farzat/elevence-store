from django.shortcuts import render
from django.views.generic import ListView, DetailView         
from .models import Product, ProductImage                  




class ProductList(ListView):       
    model = Product


class ProductDetail(DetailView):          
    model = Product

    # return extra data for product detail like image
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImage.objects.filter(product=self.get_object()) 
        return context
    