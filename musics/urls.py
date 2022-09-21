from django.urls import path
from .views import (
    HomeView, MusicDetailView, MusicLikeView, AllMusicsView, StyleListView, MusicSaveView
)



app_name = 'musics'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all-styles/', StyleListView.as_view(), name='all_styles'),
    path('all-musics/', AllMusicsView.as_view(), name='all_musics'),
    path('search/<str:search>/', HomeView.as_view(), name='home'),
    path('detail/<int:music_id>/', MusicDetailView.as_view(), name='music_detail'),
    path('like/<int:music_id>/', MusicLikeView.as_view(), name='music_like'),
    path('save/<int:music_id>/', MusicSaveView.as_view(), name='music_save'),
]
