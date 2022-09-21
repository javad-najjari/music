from rest_framework import serializers
from .models import User
from musics.models import Like, Save
from musics.serializers import LikeJustMusicSerializer, SaveSerializer



class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must be match')
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)


class UserDetailSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    saves = serializers.SerializerMethodField()
    date_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'date_joined', 'likes', 'saves')
    
    def get_likes(self, obj):
        likes = Like.objects.filter(user=obj)
        serializer = LikeJustMusicSerializer(likes, many=True)
        return serializer.data

    def get_saves(self, obj):
        saves = Save.objects.filter(user=obj)
        serializer = SaveSerializer(saves, many=True)
        return serializer.data
    
    def get_date_joined(self, obj):
        return obj.date_joined.date()



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

