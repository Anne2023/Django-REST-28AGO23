from django.db import models
from blog.models.articleEntity import ArticleEntity

class AuthorEntity(models.Model):
    name = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    articles = models.ManyToManyField(ArticleEntity, through='AuthorArticleEntity')

    def __str__(self): # equivale ao toString()
        return "Author Entity [%s]" % self.name