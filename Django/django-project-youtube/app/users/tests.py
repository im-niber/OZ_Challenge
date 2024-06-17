from django.test import TestCase
from django.contrib.auth import get_user_model

# TDD: Test Driven Development 
class UserTestCase(TestCase):

    def test_create_user(self):
        email = 'rbwo@naver.com'
        password = 'password123'

        user = get_user_model().objects.create_user(email=email, password=password)

        # 유저가 정상적으로 잘 만들어졌는지 체크
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        email = 'rbwo@naver.com'
        password = 'password123'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
