from django.contrib import admin

from .models import Customer
from .models import Product


admin.site.register(Customer)
admin.site.register(Product)
