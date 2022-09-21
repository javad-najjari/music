from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Singer
from .serializers import SingerDetailSerializer




class AllSingersView(APIView):
    def get(self, request):
        singers = Singer.objects.all()
        serializer = SingerDetailSerializer(singers, many=True)
        return Response(serializer.data)

