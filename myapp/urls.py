"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from webapp.views import *
from app_auth.views import *
from app_quiz.views import *
from quest_app.views import question

urlpatterns = [
    path('zecadmin/', admin.site.urls),
    path('',login_geead,name='login_geead'),
    path('info/<str:id>',detail,name='detail'),
    path('detail_holy_challenge/<str:id>',detail_holy,name='detail_holy_challenge'),
    path('info/recherche',search,name='search'),
    path('Holy Challenge_2022/recherche',search1,name='search1'),
    path('Holy Challenge_2023/recherche',search2,name='search2'),
    path('Holy Challenge_2024/recherche',search3,name='search3'),
    path('informations/',include("webapp.urls")),
    path('register',registrer,name='register'),
    path('Logout',Logout,name='Logout'),
    path('mon_compte',moncompte, name="mon_compte"),
    path("modifier_profile/",UpdateProfile.as_view(), name="modifier_profile"),
    path('Holy Challenge_2022',holychallenge2022, name="Holy Challenge_2022"),
    path('Holy Challenge_2023',holychallenge2023, name="Holy Challenge_2023"),
    path('Holy Challenge_2024',holychallenge2024, name="Holy Challenge_2024"),
    path('modifier_mot_de_passe/',Passwordschange.as_view(), name="modifier_mot_de_passe"),
    path("modifier_photo/",Addaccount.as_view(), name="modifier_photo"),
    path("modifier_nom/",Addaccount1.as_view(), name="modifier_nom"),
    path("modifier_numéro/",Addaccount2.as_view(), name="modifier_numéro"),
    path("modifier_filiere/<str:pk>",Addaccount3.as_view(), name="modifier_filiere"),
    path("modifier_email/",Addaccount4.as_view(), name="modifier_email"),
    path("supprimer_compte/",Deleteaccount.as_view(), name="supprimer_compte"),
    path("ajouter_commentaire/<int:pk>",Addcomment, name="ajouter_commentaire"),
    path("supprimer_commentaire/<int:pk>",Deletecomment.as_view(), name="supprimer_commentaire"),
    path('quiz biblique/',include("app_quiz.urls")),
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
