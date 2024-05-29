from django.db import models

# Create your models here.
class CommonModel(models.Model):
    #auto_now_add ? 현재 데이터 생성 시간을 기준으로 생성 -> 이후 업데이트 되어도 수정 x
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now ? 데이터 생성시에도 기준 으로 생성 -> 업데이트 되면 수정 o 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # 데이터베이스의 테이블에 위와 같은 컬럼이 추가되지 x 테이블이 추가되지 x?