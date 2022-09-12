from tkinter.tix import Tree
from django.db import models
from django.contrib.auth import get_user_model


class Location(models.Model):
    """
    locations in Jordan 
    """
    city_name = models.CharField(max_length=255)  

    def __str__(self):
        return self.city_name

class Category(models.Model): 
    """
    The type of the campaign 
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Campaign(models.Model):
    """
    The campaign information
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    date = models.DateField()
    organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="campaigns")
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=False, blank=False, on_delete=models.CASCADE)
    available_sets = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, null=True)

    def __str__(self):
        return self.title
