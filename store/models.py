from time import timezone
from django.urls import reverse
from django.db import models

from shop.settings import AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Product(models.Model):
    
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name = 'categorie', on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()
        self.orders.clear()
        super().delete(*args, **kwargs)
    def __str__(self):
        return self.user.username
