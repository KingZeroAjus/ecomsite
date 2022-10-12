from django.db import models

# Create your models here.


class Products (models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    catagory = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=400)


class Order (models.Model):
    items = models.CharField(max_length=5000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=1000)