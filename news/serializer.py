from rest_framework import serializers
from .models import Article, Keyword

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'