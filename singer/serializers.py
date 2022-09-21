from rest_framework import serializers
from .models import Singer
from musics.models import Style



class Style2Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Style
        fields = ('id', 'title')


class SingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = ('name', 'id')


class SingerDetailSerializer(serializers.ModelSerializer):
    styles = serializers.SerializerMethodField()

    class Meta:
        model = Singer
        fields = ('id', 'name', 'alias', 'birth_day', 'about', 'picture', 'styles', 'albums_of_the_singer')
    
    def get_styles(self, obj):
        style = obj.styles
        serializer = Style2Serializer(style, many=True)
        return serializer.data

