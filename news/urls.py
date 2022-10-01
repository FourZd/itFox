from django.contrib import admin
from django.urls import path, include
from .views import NewsView, CommentsView
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.SimpleRouter()
router.register(r'news', NewsView)
print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('^news/(?P<pk>[^/.]+)/comments/', CommentsView.as_view({'get': 'list', 'post': 'create'})),
    path('auth/', views.obtain_auth_token),
]