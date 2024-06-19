from rest_framework.test import APITestCase
from users.models import User
from videos.models import Video
from django.urls import reverse # url -> name을 기반으로 값을 불러옴
from rest_framework import status

from django.core.files.uploadedfile import SimpleUploadedFile


class VideoAPITestCase(APITestCase):
    
    def setUp(self):
        # 회원가입
        self.user = User.objects.create_user(
            email="rbwo@naver.com",
            password="password123"
        )
        # 로그인
        self.client.login(email="rbwo@naver.com", password="password123")
        
        self.video = Video.objects.create(
            title = "video title",
            link = "http://www.test.com",
            user = self.user
        )

    # api/v1/videos [GET]
    def test_video_list_get(self):
        url = reverse('video-list')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data) > 0, True)
        
        for video in res.data:
            self.assertIn('title', video)


    #api/v1/videos [POST]
    def test_video_list_post(self):
        url = reverse('video-list')
        data = {
            'title': 'My Test Video',
            'link': 'http://www.tets.com',
            'category': 'development',
            'thumbnail': 'http://www.test.com',
            'video_file': SimpleUploadedFile('test.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }

        res = self.client.post(url, data)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'My Test Video')


    #api/v1/videos/{video_id} [GET]
    def test_video_detail_get(self):
        url = reverse('video-detail', kwargs= {'pk':self.video.pk})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    #api/v1/videos/{video_id} [PUT]
    def test_video_detail_put(self):
        url = reverse('video-detail', kwargs= {'pk':self.video.pk})
        
        data = {
            'title': 'Update Video',
            'link': 'http://www.tets.com',
            'category': 'development',
            'thumbnail': 'http://www.test.com',
            'video_file': SimpleUploadedFile('test.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }

        res = self.client.put(url, data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['title'], 'Update Video')


    #api/v1/videos/{video_id} [DELETE]
    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs= {'pk':self.video.pk})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
