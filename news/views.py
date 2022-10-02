from multiprocessing import AuthenticationError
from django.shortcuts import render
from news.models import News, Comments, LikedNews
from rest_framework import status, permissions, viewsets, generics
from rest_framework.response import Response
from rest_framework.settings import api_settings
from .serializers import NewsSerializer, CommentsSerializer, LikesSerializer
from .permissions import IsOwnerOrReadOnly, IsAboveOwner


class NewsView(viewsets.ModelViewSet):
 
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = (
        IsOwnerOrReadOnly|permissions.IsAdminUser,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsView(viewsets.ModelViewSet):
    
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = CommentsSerializer
    permission_classes = (
        IsAboveOwner|IsOwnerOrReadOnly|permissions.IsAdminUser,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, news_id=self.kwargs['pk_news'])


    def get_queryset(self, **kwargs):
        queryset = Comments.objects.filter(news_id=self.kwargs['pk_news'])
        return queryset


class LikeView(viewsets.ModelViewSet):

    https_method_names = ['create']
    serializer_class = LikesSerializer
    permission_classes =  (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user_id = self.request.user.id
        news_id = self.kwargs['pk_news']
        lookup_field = id

        check = LikedNews.objects.filter(liked_by=user_id, liked_news=news_id)
        if(check.exists()):
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message":"Already Liked"
            })

        else:
            serializer.save(liked_by_id=user_id, liked_news_id=news_id)


    def get_queryset(self, **kwargs):
        queryset = News.objects.filter(id=self.kwargs['pk_news'])
        return queryset
    

class UnlikeView(LikeView):
    

    def perform_create(self, serializer):
        user_id = self.request.user.id
        news_id = self.kwargs['pk_news']
        lookup_field = id

        check = LikedNews.objects.filter(liked_by=user_id, liked_news=news_id)
        if(check.exists()):
            LikedNews.objects.filter(
            liked_by=user_id, liked_news=news_id
            ).delete()

        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message":"No like"
            })

    
