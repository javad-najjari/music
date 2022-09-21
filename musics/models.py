from django.db import models
from accounts.models import User



class Album(models.Model):
    title = models.CharField(max_length=250)
    album_singer = models.ForeignKey('singer.Singer', on_delete=models.CASCADE, related_name='albums')
    avatar = models.ImageField()
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)


class Music(models.Model):
    file = models.FileField(upload_to='musics')
    text = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=250, unique=True)
    avatar = models.ImageField(upload_to='music_avatar')
    singer = models.ForeignKey('singer.Singer', on_delete=models.CASCADE, related_name='musics')
    time = models.DurationField()
    style = models.ForeignKey('Style', on_delete=models.CASCADE, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musics', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)
    


class Style(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField()
    old_age = models.DateTimeField()

    def __str__(self):
        return self.title

    def short_about(self):
        return self.about[:30] + ' ...'
    
    class Meta:
        ordering = ('title',)



class Like(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Save(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
