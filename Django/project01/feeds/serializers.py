from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):

    # 이 클래스는 feed 모델들이 들어오는데,
    # feed 모델에는 user 모델도 있어서 아래 코드가 실행이 되는듯하다
    # 아래 코드를 명시적으로 작성해주면 depth 코드는 주석해도 상관업슬듯
    # 다른 foreignkey 필드가 있으면 다르겠지만

    user = FeedUserSerializer(read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Feed
        fields = "__all__"
        # 현재의 모델과 연결된 모델들까찌 직렬화 시키겠다는 뜻
        # Feed - User 모델 => 햔제 코드는 Feed 모델을 직렬화하고 있지만
        # detph = 1 코드를 통해 User 객체도 직렬화하겠다는 뜻이다

        depth = 1


class FeedDetailSerializer(ModelSerializer):
    class Meta:
        model = Feed
        # fields = ('id', 'content')
        fields = "__all__"

# 일부 데이터만 보여주는 Serialize

class ContentFeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = ('id', 'content')