from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, default="default_title")
    image = models.CharField(max_length=200, default="default_image")
    likes = models.PositiveIntegerField(default=0)

class User(models.Model):
    id = models.CharField(max_length=100, unique=True, primary_key=True)
