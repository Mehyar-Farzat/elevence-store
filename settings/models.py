from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    fb_link = models.URLField(null=True,blank=True)
    x_link = models.URLField(null=True,blank=True)
    instagram_link = models.URLField(null=True,blank=True)
    lenkedin_link = models.URLField(null=True,blank=True)


    def __str__(self):
        return self.name
    