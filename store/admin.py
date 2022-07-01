from django.contrib import admin
from  store.models import Products, Category
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display: ['name', 'price', 'category']

admin.site.register(Products)
admin.site.register(Category)

