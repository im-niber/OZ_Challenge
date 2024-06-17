from django.db import models
from common.models import CommonModel
from users.models import User

class Video(CommonModel):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField
    video_file = models.FileField(upload_to='storage/') # upload_to = 저장경로

    # User: Video 1:N 부모 자녀.
    # 유저가 삭제되면 동영상도 삭제된다
    user = models.ForeignKey(User, on_delete=models.CASCADE)
