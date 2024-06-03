from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed
from .serializers import FeedDetailSerializer, FeedSerializer

class Feeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all() # 객체

        # 객체 -> JSON 직렬화
        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data) 
    
    def post(self, request):
        serializer = FeedSerializer(data=request.data)

        # user 데이터도 필요함, 객체 자체를 전달해준다.
        if serializer.is_valid():
            feed = serializer.save(user=request.user)
            serializer = FeedSerializer(feed)
            # print("post", serializer)
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)


class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        serializer = FeedDetailSerializer(feed)
        return Response(serializer.data)