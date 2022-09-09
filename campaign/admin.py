from django.contrib import admin

from .models import Location, Campaign, Category 

admin.site.register(Campaign)
admin.site.register(Location)
admin.site.register(Category)


