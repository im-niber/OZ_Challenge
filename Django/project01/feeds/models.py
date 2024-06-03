from django.db import models
from common.models import CommonModel

# Create your models here.
# Feed와 user의 관계?  다 대 일 관계. N:1 , N 에 해당하는
# 테이블이 ForeignKey를 가짐

class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)