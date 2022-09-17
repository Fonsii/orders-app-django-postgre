from django import template
from store_app.models import Product, ProductsStore, Store

register = template.Library()

@register.simple_tag()
def spotlight_product_description():
    product_in_spotlight = ProductsStore.objects.all().first()
    return product_in_spotlight.product.description
