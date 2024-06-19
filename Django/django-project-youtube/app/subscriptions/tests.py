from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import Subscription
from django.urls import reverse

User = get_user_model()

class SubscriptionTestCase(TestCase):
    def setUp(self):
      self.user = User.objects.create_user(
         email="rbwo@naver.com",
         password="password123"
      )
      self.user2 = User.objects.create_user(
         email="rbwo1234@naver.com",
         password="password123"
      )

      self.user3 = User.objects.create_user(
         email="rbwo12345@naver.com",
         password="password123"
      )

      self.user4 = User.objects.create_user(
         email="rbwo123456@naver.com",
         password="password123"
      )
      
      self.client.login(email="rbwo@naver.com", password="password123")

      self.subscription = Subscription.objects.create(
         subscriber = self.user,
         subscribed_to = self.user2
      )
      
      self.subscription.save()

    def test_create_subscription(self):
       url = reverse('subscription-list')

       data = {
          'subscriber': self.user.pk,
          'subscribed_to': self.user4.pk
       }

       res = self.client.post(url, data=data)

       self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_subscription_to_self(self):
       url = reverse('subscription-list')

       data = {
          "subscriber": self.user,
          "subscribed_to": self.user
       }

       res = self.client.post(url, data=data)

       self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_create_duplicate_subscription(self):
        url = reverse('subscription-list')
        
        data = {
          "subscriber": self.user,
          "subscribed_to": self.user2
        }

        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_delete_subscription(self):  
        url = reverse('subscription-detail', kwargs={'pk': self.subscription.pk})
        res = self.client.delete(url)
        
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delete_nonexistent_subscription(self):
       url = reverse('subscription-detail', kwargs={'pk': 9879})
       res = self.client.delete(url)

       self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)