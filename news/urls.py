from django.contrib import admin
from django.urls import path, include
from .views import NewsView, CommentsView
from rest_framework import routers
from rest_framework.authtoken import views

news_router = routers.SimpleRouter()
news_router.register(r'news', NewsView)

comments_router = routers.SimpleRouter()
comments_router.register(r'comments', CommentsView, basename='comments')

urlpatterns = [
    path('', include(news_router.urls)),
    path('news/<int:news_pk>/', include(comments_router.urls)),
    path('auth/', views.obtain_auth_token),
]