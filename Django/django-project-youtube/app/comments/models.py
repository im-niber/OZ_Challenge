from django.db import models
from common.models import CommonModel

# - User: FK
    # -> User : Comment, Commnet, Comment o
    # -> Comment : User User User x

class Comment(CommonModel):
    # models.ManyToManyField
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    content = models.TextField(blank=False)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # 대댓글
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
