from django.forms import IntegerField
from rest_framework import serializers
from .models import News, Comments, LikedNews

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = News
        exclude = ['liked_by']

        
class CommentsSerializer(serializers.ModelSerializer):
    news_id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Comments
        fields = ['pk', 'date', 'content', 'author', 'news_id']


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedNews
        fields = ['liked_by_id', 'liked_news_id']
