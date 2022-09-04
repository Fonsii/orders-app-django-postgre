from django.db import models
from django.contrib.auth.models import User
from store_app.models import ProductsStore, Store
# Create your models here.

class Order(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductsStore)
    state = models.IntegerField() # 0: pending, 1: accepted, 2: rejected, 3:completed
