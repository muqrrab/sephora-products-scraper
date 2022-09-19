from os import link
from statistics import mode
from django.db import models

# Create your models here.


class Product(models.Model):
    group = models.CharField(max_length=20, null=True,blank=True)
    subgroup1 = models.CharField(max_length=20, null=True,blank=True)
    subgroup2 = models.CharField(max_length=20, null=True,blank=True)
    brand = models.CharField(max_length=20, null=True,blank=True)
    name = models.CharField(max_length=300, null=True,blank=True)
    price = models.CharField(max_length=20, null=True,blank=True)
    ingredient = models.TextField(null=True,blank=True)
    link = models.CharField(max_length=300, null=True,blank=True)

    def __str__(self):
        return self.name
    
class AllLinks(models.Model):
    link = models.CharField(max_length=300, null=True,blank=True)


class SingleLinks(models.Model):
    link = models.CharField(max_length=300, null=True,blank=True)

class LinktoObtain(models.Model):
    link = models.CharField(max_length=300, null=True,blank=True)

class ShortProduct(models.Model):
    group = models.CharField(max_length=20, null=True,blank=True)
    subgroup = models.CharField(max_length=20, null=True,blank=True)
    name = models.CharField(max_length=300, null=True,blank=True)
    link = models.CharField(max_length=300, null=True,blank=True)

    def __str__(self):
        return self.name