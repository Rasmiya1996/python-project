from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)


class Customer(models.Model):
    user_1 = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')
    category_id = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Item(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    in_stock = models.IntegerField()
    image = models.FileField(upload_to='images/')
    added_date = models.DateField()
    approval_status = models.IntegerField(default=0)


    def __str__(self):
        return self.product_name


class Quantity_1(models.Model):
    customer_1 = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_1 = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    add_date = models.DateField(auto_now=True)
    product_status=models.IntegerField(default=0)


class Paymoney(models.Model):
    quantity_2 = models.ForeignKey(Quantity_1, on_delete=models.CASCADE)
    address = models.TextField(max_length=150)
    total_price = models.FloatField()

    card_no = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)





class Review(models.Model):
    customer_2 = models.ForeignKey(Login, on_delete=models.CASCADE)
    date_1 = models.DateField(auto_now=True)
    review = models.TextField()
