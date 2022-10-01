from django.contrib import admin
from django.urls import path, include
from .views import NewsView, CommentsView


urlpatterns = [
    path('news/', NewsView.as_view()),
    path('<int:news_id>/comments/', CommentsView.as_view())
]