import datetime
from datetime import timezone

from django.db import models

# Create your models here.
class Question(models.Model):
    question_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_texto

    def perguntas_recentes(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Mudanca(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    mudanca_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.mudanca_text