from django.contrib import admin
from .models import *

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(CatgHoly)
admin.site.register(HolyChallenge)
admin.site.register(Addcommentaire)
admin.site.site_header = 'GEEAD INPHB Administration'
