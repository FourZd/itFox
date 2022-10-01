from rest_framework import serializers
from .models import News, Comments

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    news_id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(read_only=True)
    class Meta:
        model = Comments
        fields = ['date', 'content', 'author', 'news_id']