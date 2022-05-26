from django.contrib import admin
from .models import Favorite
from .models import Product

# Register your models here.
admin.site.register(Favorite)
admin.site.register(Product)
