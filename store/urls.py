from cgitb import lookup
from sys import builtin_module_names
from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('orders', views.OrderViewSet, basename='orders')
router.register('customers', views.CustomerViewSet)

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='products-reviews')
products_router.register('images', views.ProductImageViewSet, basename='product-images')

urlpatterns = router.urls + products_router.urls + cart_router.urls
