from audioop import avg
from datetime import datetime
from decimal import Decimal
from operator import concat, or_
from unicodedata import decimal
from django.forms import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Collection, Product, CartItem, Cart, Order, OrderItem
from tags.models import TaggedItem



# Create your views here.
def say_hello(request):
   queryset = Product.objects.raw('SELECT * FROM store_product')
   
   return render(request, 'hello.html', {'name':'Kate', 'results':list(queryset)})