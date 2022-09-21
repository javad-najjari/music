from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MusicSerializer, MusicDetailSerializer, StyleSerializer, MusicJustIdSerializer
from .models import Music, Like, Save, Style
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q




class HomeView(APIView):
    def get(self, request, search=None):
        if search is not None:
            musics = Music.objects.filter(Q(text__contains=search) | Q(title__contains=search))
            if musics.exists():
                serializer = MusicSerializer(musics, many=True)
                return Response(serializer.data)
            else:
                context = {'detail': 'no music found'}
                return Response(context, status=status.HTTP_404_NOT_FOUND)
        else:
            musics = Music.objects.all()
            popular_musics = musics.order_by('-likes')
            latest_musics = musics.order_by('-created')
            popular = MusicSerializer(popular_musics, many=True, context={'request': request})
            newest = MusicSerializer(latest_musics, many=True, context={'request': request})
            return Response({'popular': popular.data[:10], 'newest': newest.data[:10]})


class AllMusicsView(APIView):
    def get(self, request):
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)


class MusicDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, music_id):
        try:
            music = Music.objects.get(id=music_id)
            serializer = MusicDetailSerializer(music)
            return Response(serializer.data)
        except Music.DoesNotExist:
            context = {'detail': 'music was not found'}
            return Response(context, status=status.HTTP_404_NOT_FOUND)


class MusicLikeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, music_id):
        music = get_object_or_404(Music, id=music_id)
        user = request.user
        serializer = MusicJustIdSerializer(music)
        if Like.objects.filter(music=music, user=user).exists():
            Like.objects.get(music=music, user=user).delete()
            music.likes -= 1
            music.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Like.objects.create(music=music, user=user)
            music.likes += 1
            music.save()
            return Response(serializer.data, status=status.HTTP_200_OK)



class MusicSaveView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, music_id):
        music = get_object_or_404(Music, id=music_id)
        user = request.user
        serializer = MusicJustIdSerializer(music)
        if Save.objects.filter(music=music, user=user).exists():
            Save.objects.get(music=music, user=user).delete()
            music.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Save.objects.create(music=music, user=user)
            music.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class StyleListView(APIView):
    def get(self, request):
        styles = Style.objects.all()
        serializer = StyleSerializer(styles, many=True)
        return Response(serializer.data)

