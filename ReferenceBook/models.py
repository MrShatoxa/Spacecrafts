from django.db import models

# Create your models here.
class Spacecrafts(models.Model):
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    manufacturer = models.CharField(max_length=80)
    purpose = models.CharField(max_length=80)
    orbit = models.CharField(max_length=80)
    year = models.CharField(max_length=80)
    
class Article(models.Model):
    spacecrafts = models.OneToOneField(Spacecrafts, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=80)
    content = models.TextField(verbose_name="Текст статьи")
    image = models.ImageField(upload_to='images/')