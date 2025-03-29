from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(TaxModel)
admin.site.register(DiscountModel)
admin.site.register(Product)
