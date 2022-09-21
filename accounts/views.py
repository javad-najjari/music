from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserDetailSerializer
from rest_framework import status
from .models import User
from rest_framework.permissions import IsAuthenticated
from musics.models import Like, Save




class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        value = serializer.data

        if User.objects.filter(username=value['username']).exists():
            context = {'message': 'username already exists'}
            return Response(context, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=value['email']).exists():
            context = {'message': 'email already exists'}
            return Response(context, status=status.HTTP_409_CONFLICT)
        
        if value['password'] != value['password2']:
            context = {'message': 'passwords must be match'}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class RemoveAllLikesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        likes = Like.objects.filter(user=user)
        likes.delete()
        return Response(status=status.HTTP_200_OK)


class RemoveAllSavesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        saves = Save.objects.filter(user=user)
        saves.delete()
        return Response(status=status.HTTP_200_OK)





# class ChangePasswordView(UpdateAPIView):
#     serializer_class = ChangePasswordSerializer
#     model = User
#     permission_classes = (IsAuthenticated,)

#     def update(self, request):
#         user = request.user
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             if not user.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

#             if serializer.data.get('password1') == serializer.data.get('password2'):
#                 user.set_password(serializer.data.get("password1"))
#                 user.save()
#                 return Response(status=status.HTTP_200_OK)
            
#             return Response({'message': 'Inconsistency between password 1 and password 2'},
#                 status=status.HTTP_401_UNAUTHORIZED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

