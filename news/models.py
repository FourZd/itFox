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
    liked_by = models.ManyToManyField(Users, related_name="liked_news", through='LikedNews')


    @property
    def comments_count(self):
        return self.comments_set.count()


    @property
    def likes_count(self):
        return self.liked_by.count()
        

class Comments(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name = 'Date')
    content = models.TextField(verbose_name = 'Comment content')
    author = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Author')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='News')


class LikedNews(models.Model):
    liked_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    liked_news = models.ForeignKey(News, on_delete=models.CASCADE)