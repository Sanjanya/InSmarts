from rest_framework import viewsets
from .models import NewsArticle
from .serializers import NewsArticleSerializer

class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

NEWS_API_KEY = 'b9b52350120546398fcbbd1cf6ecef31'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

def fetch_news_articles(query, page_size=10):
    params = {
        'q': query,
        'apiKey': NEWS_API_KEY,
        'pageSize': page_size,
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    articles = []
    for article_data in data['articles']:
        article = NewsArticle(
            title=article_data['title'],
            content=article_data['description'],
            url=article_data['url'],
        )
        article.save()
        articles.append(article)
    return articles

def get_news_articles(request):
    query = request.GET.get('q')
    if query:
        articles = fetch_news_articles(query)
    else:
        articles = []
    context = {'articles': articles}
    return render(request, 'news/articles.html', context)