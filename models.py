from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class CatgHoly(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class HolyChallenge(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(CatgHoly,on_delete=models.CASCADE)
    categori = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.FileField(upload_to='holy_challenge')
    def __str__(self):
        return self.title 



class Article(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    desc = models.TextField()
    image = models.FileField(upload_to='photos')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mes-infos")

class Addcommentaire(models.Model):
    post = models.ForeignKey(Article, related_name="commentes", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.post.title
