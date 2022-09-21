from django.db import models
from musics.models import Album



class Singer(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, null=True, blank=True)
    birth_day = models.DateTimeField()
    about = models.TextField()
    picture = models.ImageField(upload_to='singer_picture')
    styles = models.ManyToManyField('musics.Style')
    albums_of_the_singer = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, related_name='singer')

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name
    
    def short_about(self):
        return self.about[:30] + ' ...'
    
    class Meta:
        ordering = ('name',)

