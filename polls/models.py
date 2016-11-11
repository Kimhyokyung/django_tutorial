from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('QUESTION_TEST', max_length=200)
    pub_date = models.DateTimeField('PUBLISHED DATE')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey('QUESTION', Question)
    choice_text = models.CharField('CHOICE_TEXT', max_length=200)
    votes = models.IntegerField('VOTES', default=0)

    def __str__(self):
        return self.choice_text