from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework.exceptions import ValidationError
from django.db.models import Q

class SubscriptionList(APIView):
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        if request.user.id == request.data['subscribed_to']:
            return Response("자기 자신을 구독할 수 없습니다", status=status.HTTP_400_BAD_REQUEST)
        
        subscriptions = Subscription.objects.filter(subscriber=request.user.id)

        for subscription in subscriptions:
            if subscription.subscribed_to.id == request.data['subscribed_to']:
                return Response("이미 구독중입니다", status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SubscriptionDetail(APIView):
    def delete(self, request, pk):
        try:
            subscription_obj = Subscription.objects.get(pk=pk)
        except:
            return Response("nonexistent_subscription", status=status.HTTP_400_BAD_REQUEST)
        
        subscription_obj.delete()
        return Response("", status=status.HTTP_204_NO_CONTENT)