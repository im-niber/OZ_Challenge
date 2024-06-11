from rest_framework.serializers import ModelSerializer
from .models import Address
from users.serializers import FeedUserSerializer

class AddressSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True)
    class Meta:
        model = Address
        fields = '__all__'