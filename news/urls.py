from django.urls import path
from . import views

router = views.DefaultRouter()
router.register(r'news-articles', views.NewsArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]