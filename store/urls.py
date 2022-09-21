
from django.urls import path
from . import views 
# from views import product_list

urlpatterns = [

    path('products/',views.product_list),
    path('products/<id>/',views.product_detail)
    
]
