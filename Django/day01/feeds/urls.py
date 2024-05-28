from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_feeds),
    path('all', views.all_feed),
    path("id=<int:feed_id>&content=<str:feed_content>", views.one_feed)
]
