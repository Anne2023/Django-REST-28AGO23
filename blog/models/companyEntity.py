from django.db import models
from blog.models.authorEntity import AuthorEntity

class CompanyEntity(models.Model):
    author = models.OneToOneField(
        AuthorEntity,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cnpj = models.CharField(max_length=20)

    def __str__(self): # equivale ao toString()
        return "Company Entity [%s]" % self.cnpj