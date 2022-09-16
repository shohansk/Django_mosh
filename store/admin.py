from django.contrib import admin

# Register your models here.
from .models import Cart,CartItem,Order,OrderItem,Product,Promotion,Address,Customer,Collection

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Collection)