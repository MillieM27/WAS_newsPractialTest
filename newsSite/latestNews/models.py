import datetime
from django.db import models
from django.utils import timezone


class newsArticle(models.Model):
    articleTitle = models.CharField(max_length=200)
    datePublished = models.DateTimeField('date published')
    body = models.TextField()

    def recentlyPublished(self):
        return self.datePublished >= timezone.now()
    datetime.timedelta(days=1)


    def __str__(self):
        return self.articleTitle
