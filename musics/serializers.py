from rest_framework import serializers
from .models import Music, Like, Style, Save
from singer.serializers import SingerSerializer




class StyleSerializer(serializers.ModelSerializer):
    music_count = serializers.SerializerMethodField()

    class Meta:
        model = Style
        fields = ('id', 'title', 'music_count')
    
    def get_music_count(self, obj):
        return Music.objects.filter(style=obj).count()


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()
    style = StyleSerializer()

    class Meta:
        model = Music
        fields = ('id', 'title', 'avatar', 'singer', 'likes', 'style')



class MusicDetailSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()
    style = StyleSerializer()

    class Meta:
        model = Music
        fields = '__all__'


class MusicJustIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id',)


class MusicDetail2Serializer(serializers.ModelSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Music
        fields = ('id', 'title', 'avatar', 'singer')


class LikeJustMusicSerializer(serializers.ModelSerializer):
    music = MusicDetail2Serializer()

    class Meta:
        model = Like
        fields = ('music',)


class SaveSerializer(serializers.ModelSerializer):
    music = MusicDetail2Serializer()

    class Meta:
        model = Save
        fields = ('music',)

