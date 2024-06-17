from django.db import models
from common.models import CommonModel

class Subscription(CommonModel):
    # realted_name은 역참조를 하기 때문에 네이밍을 반대로해주는게 이해가 편함
    # user를 다 참조하므로, user.subscriptions.all() 하면 내가 구독하는 목록이 나오며,
    # user.subscribers.all() 하면 나를 구독하는 사용자들이 나온다.
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers')
