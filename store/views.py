from django.shortcuts import render

from store.models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={"products": products})