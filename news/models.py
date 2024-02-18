from django.db import models
import spacy

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    keywords = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

nlp = spacy.load('en_core_web_sm')

def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.lemma_.lower().strip() for token in doc if token.is_stop != True and token.is_punct != True]
    return ', '.join(keywords)

NewsArticle.add_to_class('keywords', property(extract_keywords))