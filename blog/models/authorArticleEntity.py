from django.db import models
from blog.models.articleEntity import ArticleEntity
from blog.models.authorEntity import AuthorEntity

class AuthorArticleEntity(models.Model):
    author = models.ForeignKey(AuthorEntity, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleEntity, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): # equivale ao toString()
        return "AuthorArticle Entity [%x]" % self.created