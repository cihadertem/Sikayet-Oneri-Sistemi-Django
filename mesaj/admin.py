from django.contrib import admin

from .models import hizmetTur,Tur, Post


@admin.register(Tur)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model=Tur

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['mesajTuru','baslik','doktor','alinanHizmet','sikayet','sikayetciMail','sikayetTarihi']

    class Meta:
        model=Post

@admin.register(hizmetTur)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model=hizmetTur

