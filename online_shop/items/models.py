import django.utils.timezone
from django.db import models
import datetime

class Producer(models.Model):
    produser_name = models.CharField(max_length=120)
    def __str__(self):
        return self.produser_name

class Items(models.Model):
    item_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    producer = models.ForeignKey(to=Producer,on_delete=models.CASCADE, null=True)
    slug=models.SlugField(max_length=255, unique=True, db_index=True)


class AddUser(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    age = models.IntegerField()

