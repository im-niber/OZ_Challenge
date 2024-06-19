from django.urls import path
from .views import VideoDetail, VideoList

# api/v1/videos - VideoList
# api/v1/videos/{video_id}
urlpatterns = [
    path('', VideoList.as_view(), name='video-list'),
    path('<int:pk>', VideoDetail.as_view(), name='video-detail'),
]