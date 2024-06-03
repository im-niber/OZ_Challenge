from rest_framework.serializers import ModelSerializer
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import User

class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_superuser',)
        # extra_kwargs = {
        #     'username': {
        #         'validators': [UnicodeUsernameValidator()],
        #     }
        # }

class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
