from django.urls import path,include
from .views import *


urlpatterns = [
    path("",question, name="question"),
]
