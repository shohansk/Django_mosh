from multiprocessing import context
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store import serializers
from .serializers import ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from store.models import OrderItem, Product
# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = serializers.ProductSerializer(
        queryset,many =True,context = {'request':request}
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.validated_data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    
    # return Response('hello')

@api_view(['GET','PUT','DELETE'])
def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method== 'GET':
       queryset = Product.objects.select_related('collection').all()
       serializer = ProductSerializer(product)
       return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if product.orderitems_set.count() > 0:
            return Response({'error':'product can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # return Response(id)