from django.db import models
from django.contrib.auth.models import User
from store_app.models import ProductsStore, Store
# Create your models here.

STATE_CHOICES = (
    ('REQUESTED', 'REQUESTED'),
    ('ACCEPTED', 'ACCEPTED'),
    ('REJECTED', 'REJECTED'),
    ('COMPLETED', 'COMPLETED'),

)
class Order(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductsStore)
    state = models.CharField(max_length=10, choices=STATE_CHOICES)
