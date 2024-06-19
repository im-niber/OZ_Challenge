from rest_framework import serializers
from .models import Video
from users.serializers import UserInfoSerializer
from comments.serializers import CommentSerializer
from reactions.models import Reaction

class VideoListSerializer(serializers.ModelSerializer):

    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'
        # depth = 1

class VideoDetailSerializer(serializers.ModelSerializer):
    # 이름 맞춰야함 (중요)
    reactions = serializers.SerializerMethodField()
    
    # Video:Comment(FK-자녀 들고있는게 자녀임) 
    # Reverse Accessor = 부모가 자녀를 찾을 때 필요
    # 아래 _set 붙여줘야함. 다르게 하고 싶다면 모델 선언에서 realted_name 설정하믄댐
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'

    def get_reactions(self, obj):
        return Reaction.get_video_reactions(obj)