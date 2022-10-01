from django.shortcuts import render
from news.models import News, Comments
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import NewsSerializer, CommentsSerializer
from django.contrib.auth.models import Permission

class NewsView(generics.GenericAPIView):
    serializer_class = NewsSerializer
    http_method_names = ['get', 'post']


    def get_queryset(self):
        return News.objects.all()

    def get(self, request, format=None):
        users = News.objects.all()
        serializer = NewsSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        self.http_method_names.append("GET")

        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsView(generics.GenericAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.all()
     