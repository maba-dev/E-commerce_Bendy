from django.contrib import admin
from  store.models import Product, Category, Order, Cart
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Cart)

