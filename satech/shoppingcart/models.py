from decimal import Decimal
from distutils.command.upload import upload
# from itertools import product
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='pics')
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()

    def __str__(self):
        return (self.name)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    coupon = models.ForeignKey("Coupon",on_delete=models.SET_NULL, blank=True,null=True)
    discount = models.ForeignKey("Coupon", on_delete=models.SET_NULL,blank=True,null=True, related_name="discounted")
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        # if self.coupon:
        #     discounted_price = sum([item.get_total for item in orderitems]) - sum([item.get_total for item in orderitems]) * self.discount/100
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def fullTotal(self):
        discounted_price = self.discount * self.get_cart_total()
        total = self.get_cart_total() - discounted_price
        return total,discounted_price
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)

    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    active = models.BooleanField()

    def __str__(self):
        return self.code

    # @property
    # def coupon(self):
    #     if self.coupon_id:
    #         return Coupon.objects.get(id=self.coupon_id)
    #     return None

    # @property
    # def discount(self):
    #     if self.coupon:
    #         discounted_price = self.product.price
        

    # @property
    # def get_total_price_after_discount(self):
    #     return self.get_cart_total() - self.get_discount()



    # discount_percent = models.FloatField(default=10)
    # coupon_code = models.CharField(max_length=20)
    # quantity = models.IntegerField()
   
     


# class Order(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
#     order = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    
    
      