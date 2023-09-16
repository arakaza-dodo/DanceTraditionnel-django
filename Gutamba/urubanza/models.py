from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class agenda(models.Model):
   date = models.DateField()
   time = models.TimeField()

class Meta():
       verbose_name_plural = "agenda"   

class Club(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adress = models.CharField(max_length=15)
    agenda = models.ForeignKey(agenda ,null=False ,on_delete=models.PROTECT)
    style_de_danse = models.CharField(max_length=100)
    Client= models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom
    
class Meta():
       verbose_name_plural = "Club"
    
class Video(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Meta():
       verbose_name_plural = "Video"    

