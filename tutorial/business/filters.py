from django_filters import FilterSet
from .models import Product


class ProductFilter(FilterSet):
   class Meta:
       model = Product
       fields = {
           'product_name': ['icontains'],
           'start_date': ['gt'],
           'price': ['lt','gt',],
       }
