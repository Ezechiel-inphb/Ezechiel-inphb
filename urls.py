from django.urls import path,include
from .views import *
from django.contrib import admin


urlpatterns = [
    path("",home, name="home"),
    path('zecadmin/', admin.site.urls),
    path('info/<str:id>/',detail,name='detail'),
    path('detail_holy_challenge/<str:id>',detail_holy,name='detail_holy_challenge'),
    path("ajouter_commentaire/<int:pk>",Addcomment, name="ajouter_commentaire"),
    path("supprimer_commentaire/<int:pk>",Deletecomment.as_view(), name="supprimer_commentaire"),
    #path('Holy Challenge_2022',holychallenge2022, name="Holy Challenge_2022"),
    #path('Holy Challenge_2023',holychallenge2023, name="Holy Challenge_2023"),
    #path('Holy Challenge_2024',holychallenge2024, name="Holy Challenge_2024"),
]
