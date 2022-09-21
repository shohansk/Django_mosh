
from django.urls import path
from . import views 
# from views import product_list

urlpatterns = [

    # path('products/',views.product_list,name='Product'),
    path('products/',views.ProductList.as_view(),name='Product'),
    path('collections/',views.collections_list,name='Collection'),
    # path('products/<id>/',views.product_detail,name='Product')
    path('products/<int:pk>/',views.ProductDetail.as_view(),name='Product')
    
]
