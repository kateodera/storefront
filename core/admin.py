from itertools import product
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin, ProductImageInline
from store.models import Product
from tags.models import TaggedItem
from .models import User

# Register your models here.
@admin.register(User)
class User(BaseUser):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )

class TagInline(GenericTabularInline):
    model=TaggedItem
    autocomplete_fields=['tag']
    max_num = 10
    min_num = 1
    extra = 0

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline, ProductImageInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)