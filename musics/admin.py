from django.contrib import admin
from .models import Album, Music, Style, Like, Save



@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'album_singer')
    list_filter = ('album_singer',)
    search_fields = ('title', 'album_singer')


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'singer', 'time', 'style')
    list_filter = ('singer',)
    search_fields = ('title', 'singer')


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('title', 'old_age', 'short_about')
    search_fields = ('title',)



@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('music', 'user')
    search_fields = ('music',)



@admin.register(Save)
class SaveAdmin(admin.ModelAdmin):
    list_display = ('music', 'user')
    search_fields = ('music',)

