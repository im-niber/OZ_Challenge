from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q

# User : Reaction -> user: reaciton 1 : N
# Video : Reaction 1 : N

class Reaction(CommonModel):
    # User 모듈을 불러오지않고도 가능하다
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    # LIKE(1) DISLIKE(-1) NO_REACTION(0)
    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    @staticmethod
    def get_video_reactions(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count=Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count=Count('pk', filter=Q(reaction=Reaction.DISLIKE))
        )
        
        return reactions