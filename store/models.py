import email
from django.db import models

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=10,primary_key=True) 
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    las_update = models.DateField(auto_now_add=True)

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