from django.shortcuts import render
import requests
from .keyword_extractor import extract_keywords
from .models import NewsArticle
from django.views.generic import ListView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import NewsArticle
from .serializers import NewsArticleSerializer

# ...

class NewsAPIView(APIView):
    authentication_classes = (SessionAuthentication)
# Create your views here.
import json

def get_news_articles(request):
    query = request.GET.get('q')
    if query:
        articles = fetch_news_articles(query)
    else:
        articles = []
    data = {'articles': [article.serialize() for article in articles]}
    return JsonResponse(data)




