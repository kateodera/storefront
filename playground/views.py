from audioop import avg
from datetime import datetime
from decimal import Decimal
from email import message
from operator import concat, or_
from unicodedata import decimal
from django.forms import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Collection, Product, CartItem, Cart, Order, OrderItem
from tags.models import TaggedItem
from .tasks import notify_customers

import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
import logging

# Create your views here.
logger = logging.getLogger(__name__)

#class HelloView(APIView):
   #@method_decorator(cache_page(timeout=5*60))
def say_hello(request):
   try:
      logger.info('Calling Httpbin')
      response = requests.get('https://httpbin.org/delay/2')
      logger.info('Received response')
      data = response.json()
   except ConnectionError:
      logger.critical('Httpbin is offline')
   return render(request, 'hello.html', {'name': 'Kate'})


   