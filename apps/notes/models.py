from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


class Note(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=100)
    content = models.TextField('Conteúdo')

    class Meta:
        ordering = ['title']
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'

    def __str__(self):
        return self.title
