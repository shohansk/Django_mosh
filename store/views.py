from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from .serializers import CollectionSerializer, ProductSerializer
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from django.shortcuts import get_object_or_404

from store.models import Collection, OrderItem, Product
# Create your views here.


# class based view

class ProductList(APIView):
    def get(self,request):
        queryset = Product.objects.select_related('collection').all()
        serializer = serializers.ProductSerializer(
        queryset,many =True,context = {'request':request}
        )
        return Response(serializer.data)
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.validated_data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)



class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductDetail(APIView):
#     def get(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         serializer = ProductSerializer(Product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         if Product.orderitems_set.count() > 0:
#             return Response({'error':'product can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
#         Product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# funtion based View

# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = serializers.ProductSerializer(
#         queryset,many =True,context = {'request':request}
#         )
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # print(serializer.validated_data)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

    
    # return Response('hello')

# @api_view(['GET','PUT','DELETE'])
# def product_detail(request,id):
#     product = get_object_or_404(Product,pk=id)
#     if request.method== 'GET':
#        queryset = Product.objects.select_related('collection').all()
#        serializer = ProductSerializer(product)
#        return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         if product.orderitems_set.count() > 0:
#             return Response({'error':'product can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    # return Response(id)

class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    # def delete(self,request,pk):
    #     collection = get_object_or_404(Collection,pk=pk)
    #     if collection.count() > 0:
    #         return Response({'error':'product can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def collections_list(request):
#     if request.method == 'GET': 
#         queryset = Collection.objects.all()
#         serializer = serializers.CollectionSerializer(queryset,many=True)
#     # serializer.is_valid(raise_exception=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # print(serializer.validated_data)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

    
