from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
   username = models.CharField(max_length = 50, unique=True)
   password = models.CharField(max_length = 256)

class News(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Date')
    headline = models.CharField(max_length=150, verbose_name='Headline')
    content = models.TextField(verbose_name='News content')
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

class Comments(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name = 'Date')
    content = models.TextField(verbose_name = 'Comment content')
    author = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Author')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='News')