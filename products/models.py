from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='product')
    price = models.FloatField()
    sku = models.CharField(max_length=10)
    description = models.TextField(max_length=2000)
    




class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product_images')
    



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='review_user')
    product = models.ForeignKey(Product, related_name='review_product', on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)