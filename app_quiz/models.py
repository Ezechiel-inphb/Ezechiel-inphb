from django.db import models
from django.contrib.auth.models import User
import random

"""class Quiz(models.Model):
    name = models.CharField(max_length=200)
    number_of_quest = models.IntegerField()
    time = models.IntegerField(help_text="La durée du quiz en minutes")
    score_to_pass = models.IntegerField(help_text="le score en %")

    def __str__(self):
        return f"{self.name}"
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_quest]"""

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number_of_quest = models.IntegerField()
    time = models.IntegerField(help_text="La durée du quiz en minutes")
    score_to_pass = models.IntegerField(help_text="le score en %")

    def __str__(self):
        return f"{self.name}"
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_quest]

    
