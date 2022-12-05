from django.db import models
class Post(models.Model):
    ad = models.CharField(max_length=50, blank=True, null=True, verbose_name='Adınız(İsteğe Bağlı)')
    mesajTuru = models.ForeignKey('Tur', on_delete=models.CASCADE,blank=False,null=False,verbose_name='Tür(Zorunlu)')
    doktor = models.CharField(max_length=50,blank=True,null=True, verbose_name='Doktor İsmi')
    alinanHizmet = models.ForeignKey('hizmetTur', on_delete=models.CASCADE,blank=True,null=True,verbose_name='Alınan Hizmet Türü')
    baslik = models.CharField(max_length=120, verbose_name='Başlık')
    sikayet = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    sikayetciMail = models.EmailField(max_length=254 ,blank=True,null=True,verbose_name='Mail Adresi(İsteğe Bağlı)')
    #sikayetciNumara = models.EmailField(max_length=254, blank=True, null=True, verbose_name='Telefon Numarası(İsteğe Bağlı)')
    sikayetTarihi = models.DateTimeField(verbose_name="Yayınlanma Tarihi", auto_now_add=True)
    class Meta:
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
class Tur(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Şikayet Tür"
        verbose_name_plural = "Şikayet Türleri"

class hizmetTur(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Hizmet Türü"
        verbose_name_plural = "Hizmet Türleri"
# Create your models here.
