from rest_framework import serializers
from .models import Product ,Brand


class productserializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= '__all__'

class brandserializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields= '__all__'