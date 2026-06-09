from django.core.cache import cache
from django.shortcuts import get_object_or_404
from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_prod_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'prod_list'
    prod = cache.get(key)
    if prod is not None:
        return prod
    prod = Product.objects.all()
    cache.set(key, prod)
    return prod

def get_products_by_category(category_name: str):
    category = get_object_or_404(Category, name=category_name)
    return Product.objects.filter(category=category)
