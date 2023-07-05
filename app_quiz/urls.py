from django.urls import path
from .views import *

urlpatterns = [
    path("",jeu_biblique, name="jeu_biblique"),
    path("data",quest_data, name="quest_data"),
    path("save/",save_quiz, name="save_quiz"),
]