from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import productserializers

@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    data = productserializers(products,many=True,context={'request':request}).data
    return Response({'products':data})


@api_view(['GET'])
def product_detail_api(request,product_id):
    products = Product.objects.get(id=product_id)
    data = productserializers(products,context={'request':request}).data
    return Response({'product':data})