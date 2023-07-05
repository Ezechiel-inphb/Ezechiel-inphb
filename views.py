from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse
from .forms import CommentForms
from app_auth.models import Compteetu
from django.views.generic.edit import *
from app_auth.encryption_util import *


def home(request):
    list_article = Article.objects.all()
    list_art = []
    for art in list_article:
        art.encrypt_key = encrypt(art.id)
        art.id = art.id
        list_art.append(art)
    context = {"list_article":list_art}
    return render(request,"index.html",context)

def detail(request,id):
    id = decrypt(id)
    article = Article.objects.get(id=id)
    category = article.category
    article_relation = Article.objects.filter(category = category)[:5]
    account = Compteetu.objects.all()
    return render(request,"detail.html",{"article":article,"aer":article_relation,"account":account})

def search(request):
    query = request.GET["info"]
    list_article = Article.objects.filter(title__icontains=query)
    return render(request,"search.html",{"list_article":list_article})

def Addcomment(request, pk):
    article = Article.objects.get(id=pk)
    form = CommentForms(instance=article)
    if request.method == "POST":
        form = CommentForms(request.POST, instance=article)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data["content"]
            c = Addcommentaire(name=name, post=article, content=body)
            c.save()

        return redirect('home')
    else:
        form = CommentForms()

    context = {'form': form}

    return render(request, "add_comment.html", context)


class Deletecomment(DeleteView):
    model = Addcommentaire
    success_url = "/acceuill/"

def holychallenge2022(request):
    HoCh = HolyChallenge.objects.all()
    list_art = []
    for art in HoCh:
        art.encrypt_key = encrypt(art.id)
        art.id = art.id
        list_art.append(art)
    return render(request,"holy2022.html",{'holy':list_art})

def holychallenge2023(request):
    HoCh = HolyChallenge.objects.all()
    list_art = []
    for art in HoCh:
        art.encrypt_key = encrypt(art.id)
        art.id = art.id
        list_art.append(art)
    return render(request,"holy2023.html",{'holy':list_art})

def holychallenge2024(request):
    HoCh = HolyChallenge.objects.all()
    list_art = []
    for art in HoCh:
        art.encrypt_key = encrypt(art.id)
        art.id = art.id
        list_art.append(art)
    return render(request,"holy2024.html",{'holy':list_art})

def search1(request):
    query = request.GET["info"]
    list_holy = HolyChallenge.objects.filter(title__icontains=query)
    return render(request,"search1.html",{"list_holy":list_holy})

def search2(request):
    query = request.GET["info"]
    list_holy = HolyChallenge.objects.filter(title__icontains=query)
    return render(request,"search2.html",{"list_holy":list_holy})

def search3(request):
    query = request.GET["info"]
    list_holy = HolyChallenge.objects.filter(title__icontains=query)
    return render(request,"search3.html",{"list_holy":list_holy})

def detail_holy(request,id):
    id = decrypt(id)
    hl = HolyChallenge.objects.get(id=id)
    return render(request,"detail1.html",{"hl":hl})
    



