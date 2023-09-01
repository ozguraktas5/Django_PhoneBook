from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

class Person(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/persons', blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = "Kişi"
        verbose_name_plural = "Kişiler"
        ordering = ['id']
    
class Location(models.Model):
    name = models.CharField(max_length=75)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Lokasyon"
        verbose_name_plural = "Lokasyonlar"
        
class UploadImage(models.Model):
    image = models.ImageField(upload_to="persons")
