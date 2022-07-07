
from itertools import product
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import DefaultPagination
from rest_framework import status
from .models import Collection, Product, OrderItem, Review
from .serializers import CollectionSerializer, ProductSerializer, ReviewSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    filterset_fields = ['collection_id']
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    def get_serializer_context(self):
        return {'request':self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id = kwargs['pk']).count() > 0:
            return Response({'error':'Product can not be deleted as it is related to an order Item'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_serializer_context(self):
        return {'request':self.request}
    
    def destroy(self, request, *args, **kwargs):
        if Collection.objects.filter(product_id = kwargs['pk']).count()>0:
            return Response({'error':'Products related to this collection still exists'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
    
    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])
    
    def destroy(self, request, *args, **kwargs):
        if Review.objects.filter(product_id = kwargs['pk']).count()>0:
            return Response({'error':'Products related to this collection still exists'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)