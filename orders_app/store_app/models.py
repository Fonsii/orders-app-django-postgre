from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
    store = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    ref = models.CharField(max_length=100)


class ProductsStore(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class TagsStore(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
