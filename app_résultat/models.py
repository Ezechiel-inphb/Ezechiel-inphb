from django.db import models
from app_quiz.models import Game
from django.contrib.auth.models import User


class Result(models.Model):
    quiz = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)
