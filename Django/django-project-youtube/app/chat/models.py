from django.db import models
from users.models import User
from common.models import CommonModel

class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)