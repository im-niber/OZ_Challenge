from rest_framework.views import APIView
from .models import Video
from .serializers import VideoListSerializer, VideoDetailSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        # 직렬화 object -> json
        serializer = VideoListSerializer(videos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        
        # 역직렬화
        serializer = VideoListSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetail(APIView):
    def get(self, request, pk):
        try:
            video_obj = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound
        
        serializer = VideoDetailSerializer(video_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        video_obj = Video.objects.get(pk=pk)
        user_data = request.data

        # 앞에 있는 데이터를 뒤에 있는 데이터로 업데이트 하겠다는 의미
        serializer = VideoDetailSerializer(video_obj, user_data)

        # 위에서 올바른 데이터를 확인하는 코드를 한 줄에 하는 코드
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        video_obj = Video.objects.get(pk=pk)
        video_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)