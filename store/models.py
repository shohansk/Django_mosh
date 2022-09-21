  
from xml.sax.handler import feature_external_ges
from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self) -> str:
        return self.description

class Collection(models.Model):
    tittle = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')
    def __str__(self) -> str:
        return self.tittle
 
class Product(models.Model):
    sku = models.CharField(max_length=10,primary_key=True) 
    slug = models.SlugField()
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    las_update = models.DateField(auto_now_add=True)
    promotions = models.ManyToManyField(Promotion)

    def __str__(self) -> str:
        return self.tittle

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SLIVER = 'S'
    MEMBERSHIP_GOLD ='G'
    MEMBERSHIP_CHOICES = [
        ('MEMBERSHIP_BRONZE','Bronze'),
        ('MEMBERSHIP_SLIVER','Sliver'),
        ('MEMBERSHIP_GOLD','Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=100,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

    def __str__(self) -> str:
        return self.first_name



class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed')
    
    ]

    placed_at = models.DateTimeField(auto_now_add=True)

    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
    
    def __str__(self) -> str:
        return self.payment_status

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    coustomer = models.ForeignKey(Customer,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.street

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name='orderitems')
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2) 

    def __str__(self) -> str:
        return self.order

class Cart(models.Model):
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.created_at


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.cart


