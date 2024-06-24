from rest_framework.views import APIView
from .models import ChatMessage, ChatRoom
from .serializers import ChatMessageSerializer, ChatRoomSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def show_html(request):
    return render(request, 'index.html')

class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)        

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        serializer = ChatRoomSerializer(data=user_data)      

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

# ChatMessage
# [GET]: 특정 채팅방의 채팅 내역 -> 카카오 채팅 서버(채팅 내역을 로컬에 저장)
# [POST]: 채팅 메세지 생성
class ChatMessageList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(room=chatroom, sender=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)