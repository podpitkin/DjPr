from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, catalog_list, prod_detail

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('',catalog_list, name='prod_list'),
    path('products/<int:pk>/',prod_detail, name='prod_detail')
]
