from django.db import models
from blog.models.authorEntity import AuthorEntity

class PersonEntity(models.Model):
    author = models.OneToOneField(
        AuthorEntity,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cpf = models.CharField(max_length=20)

    def __str__(self): # equivale ao toString()
        return "Person Entity [%s]" % self.cpf