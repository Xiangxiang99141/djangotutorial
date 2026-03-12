from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #CASCADE問題珊除，選項一起刪除
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)