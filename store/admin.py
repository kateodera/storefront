from itertools import count
from django.contrib import admin, messages
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = models.ProductImages
    max_num = 10
    min_num = 1
    extra = 0
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src ="{instance.image.url}" class="thumbnail"/>')
        return ''

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    search_fields=['title']
    prepopulated_fields ={
        'slug':['title']
    }
    autocomplete_fields = ['collection']
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status','collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_filter=['collection', 'last_update']
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated',
            messages.ERROR
        )
    
    class Media:
        css = {
            'all':['store/style.css']
        }

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ['first_name', 'last_name', 'membership_model', 'orders']
    list_editable = ['membership_model']
    list_per_page = 10
    ordering= ['user__first_name', 'user__last_name']
    search_fields = ['user__first_name__istarts_with', 'user__last_name__istarts_with']

    @admin.display(ordering='orders')
    def orders(self, customer):
       url = (reverse('admin:store_order_changelist') 
        + '?' 
        + urlencode({ 'customer__id': str(customer.id)
        }))
       return format_html('<a href = {}>{}</a>', url,customer.orders)
        
    

    def get_queryset(self, request) :
        return super().get_queryset(request).annotate(
           orders = Count('order')
       )


class OrderItemInline(admin.StackedInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model=models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields=['customer']
    inlines = [OrderItemInline]
    list_display = ['id','placed_at', 'payment_status', 'customer']
    list_per_page = 10
    list_select_related = ['customer']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields=['title']
    list_display =  ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
       url = (reverse('admin:store_product_changelist') 
        + '?' 
        + urlencode({ 'collection__id': str(collection.id)
        }))
       return format_html('<a href = {}>{}</a>', url,collection.products_count)
        


    def get_queryset(self, request) :
        return super().get_queryset(request).annotate(
           products_count = Count('product')
       )


