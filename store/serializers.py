from dataclasses import fields
from rest_framework import serializers
from .models import Product,Collection
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['tittle','description','slug','inventory','price']
        fields ='__all__'
    

    def create(self, validated_data): 
        return super().create(validated_data)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields ='__all__'