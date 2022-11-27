from django.db import models
class Post(models.Model):
    mesajTuru = models.ForeignKey('Tur', on_delete=models.CASCADE,blank=False,null=False,verbose_name='Tür(Zorunlu)')
    baslik = models.CharField(max_length=120,verbose_name='Başlık')
    doktor = models.CharField(max_length=50,blank=True,null=True, verbose_name='Doktor İsmi')
    alinanHizmet = models.ForeignKey('hizmetTur', on_delete=models.CASCADE,blank=True,null=True,verbose_name='Alınan Hizmet Türü')
    sikayet = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    sikayetciMail = models.EmailField(max_length=254 ,blank=True,null=True,verbose_name='Mail Adresi(İsteğe Bağlı)')
    #sikayetciNumara = models.EmailField(max_length=254, blank=True, null=True, verbose_name='Telefon Numarası(İsteğe Bağlı)')
    sikayetTarihi = models.DateTimeField()
class Tur(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class hizmetTur(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name
# Create your models here.
