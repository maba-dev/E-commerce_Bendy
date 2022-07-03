from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
  
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
  
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
