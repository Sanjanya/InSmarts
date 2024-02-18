
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    keywords = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            'title': self.title,
            'content': self.content,
            'url': self.url,
        }
    def save(self, *args, **kwargs):
        self.keywords = extract_keywords(self.content)
        super(NewsArticle, self).save(*args, **kwargs)