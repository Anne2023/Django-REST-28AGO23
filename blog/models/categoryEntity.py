from django.db import models

class CategoryEntity(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self): # equivale ao toString()
        return "Category Entity [%s]" % self.category