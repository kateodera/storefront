import collections
from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from urllib import request
from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
    
    products_count = serializers.SerializerMethodField(method_name='product_count', read_only=True)

    def product_count(self, collection:Collection):
        return collection.product.count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','unit_price','slug','description', 'inventory','price_with_tax', 'collection']
    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
   

    def calculate_tax(self, product:Product):
        return product.unit_price * Decimal(1.1)

    def __str__(self):
        return self.collection

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','name', 'description', 'date']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)


        
