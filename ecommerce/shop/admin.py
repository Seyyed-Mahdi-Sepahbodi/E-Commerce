from django.contrib import admin
from .models import StoreType, Tag, Store, Product

# Register your models here.


@admin.register(StoreType)
class StoreTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass