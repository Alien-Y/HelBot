from django.db import models


class QuestionModel(models.Model):
    question = models.CharField(max_length=255, null=False)


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)