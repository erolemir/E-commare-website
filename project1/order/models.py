from django import forms
from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.

class ShopCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.product.title
    
    @property #Burada bir sütun ile işlem yapmak istediğimizde property kullanıyoruz.
    def amount(self):
        return (self.quantity * self.product.price)
    
    @property
    def price(self):
        return(self.product.price)
    
class ShopCardForm(forms.ModelForm):
    class Meta:
        model = ShopCard
        fields = ['quantity']
        
class Order(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Preparing','Preparing'),
        ('OnShipping','OnShipping'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    username = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    total = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username','phone','address','city','country']

class OrderProduct(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Canceled','Canceled'),
    )
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.title