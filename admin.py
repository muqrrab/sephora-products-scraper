from itertools import product
from textwrap import shorten
from django.contrib import admin
from .models import Product,AllLinks,SingleLinks,LinktoObtain,ShortProduct
# Register your models here.

admin.site.register(Product)
admin.site.register(AllLinks)
admin.site.register(SingleLinks)
admin.site.register(LinktoObtain)
admin.site.register(ShortProduct)
