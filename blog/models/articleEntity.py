from django.db import models
from blog.models.categoryEntity import CategoryEntity

class ArticleEntity(models.Model):
    title = models.CharField(max_length=64)
    subject = models.CharField(max_length=128) 
    content = models.TextField()
    category = models.ForeignKey(CategoryEntity, on_delete=models.CASCADE)

    def __str__(self): # equivale ao toString()
        return "Article Entity [%s]" % self.title