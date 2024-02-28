from django.shortcuts import render
from product.models import Product,Brand,Review
from django.db.models import Count

# Create your views here.
def Home(request):
    brands=Brand.objects.all(). annotate(product_count=Count('product_brand'))
    sale_products= Product.objects.filter(flag='Sale')[:10]
    featured_products= Product.objects.filter(flag='Featured')[:6]
    new_products= Product.objects.filter(flag='New')[:10]
    reviews= Review.objects.all()[:5]



    return render (request,'setting/Home.html',{
        'brands':brands,
        'sale_products':sale_products,
        'featured_products':featured_products,
        'new_products':new_products,
        'reviews':reviews,



    })