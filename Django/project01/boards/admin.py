from django.contrib import admin
from .models import Board

# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("title", "writer", "date", "likes", "created_at", "updated_at")

    list_filter = ("date", "writer")

    search_fields = ("title", "content")

    # 순서
    ordering = ("-date", )

    # 사용자가 수정 불가능한 컬럼 정할수있음
    readonly_fields = ("writer", )

    # 상세 정보의 뷰 형태
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('Advanced options', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
    )

    # 한 번에 보이는 페이지수
    list_per_page = 10

    # 아래 함수를 어드민 페이지에서 지정할 수 있음.
    # 설명은 맨 아래의 문장과 같음.
    actions = ("increment_likes",)
    def increment_likes(self, request, queryset):
        # 선택된 게시글들에 대해 'likes' 수를 1씩 증가
        for board in queryset:
            board.likes += 1
            board.save()
    increment_likes.short_description = "선택된 게시글의 좋아요 수 증가"