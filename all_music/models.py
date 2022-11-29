from django.db import models
from authentication.models import userInfo


class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title

class Playlist(models.Model):
    user = models.ForeignKey(userInfo, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ManyToManyField(Song)
    image = models.ImageField(null=True,blank=True)
    
