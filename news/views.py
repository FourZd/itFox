from multiprocessing import AuthenticationError
from django.shortcuts import render
from news.models import News, Comments, Users
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.settings import api_settings
from .serializers import NewsSerializer, CommentsSerializer


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, 
    )


class CommentsView(viewsets.ModelViewSet):
    
    serializer_class = CommentsSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, news_id=self.kwargs['news_pk'])

    def get_queryset(self, **kwargs):
        queryset = Comments.objects.filter(news_id=self.kwargs['news_pk'])
        return queryset
