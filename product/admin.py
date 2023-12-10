from django.contrib import admin
from .models import Product,Productimage,Review,Brand
# Register your models here.

class ProductImageTabular(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Productimage


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','flag','quantity','price']
    search_fields=['name','price','subtitle']
    list_filter=['name','price','flag']
    inlines = [ProductImageTabular]
admin.site.register(Review)
admin.site.register(Brand)
admin.site.register(Productimage)
admin.site.register(Product,ProductAdmin)