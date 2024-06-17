from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.db import models

class UserManager(BaseUserManager):
    # 일반 유저 생성 함수
    def create_user(self, email, password):
        if not email:
            raise ValueError("이메일이 필요합니다")
        
        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=20)
    is_business = models.BooleanField(default=False)

    # Permissons Mixin: 유저 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # AbstractBaseUser 모델에서,  Username은 필수인데 그걸 email로 설정, 이메일은 유니크로해야한다
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self) -> str:
        return f'email {self.email}, nickname: {self.nickname}'
