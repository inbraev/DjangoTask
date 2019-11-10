import json
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from course.models import Course, Category
from django.urls import reverse
from course.serializers import CourseSerializer

client = APIClient()


class CourseTestGetAll(APITestCase):

    def test_course_get_all(self):
        response = client.get('/course/')
        categories = Course.objects.all()
        serializer = CourseSerializer(categories, many=True)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK


class CourseTestGetSingle(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Programming', imgpath='test')
        self.course = Course.objects.create(name='English', description='test', category=self.category, logo='test')

    def test_Course_get_valid_single(self):
        url = reverse('CourseDetailUrl', kwargs={'pk': self.course.pk})
        response = client.get(url)
        course = Course.objects.get(pk=self.course.pk)
        serializer = CourseSerializer(course)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK

    def test_Course_get_invalid_single(self):
        url = reverse('CourseDetailUrl', kwargs={'pk': 770})
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND


class CourseTestPost(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Programming', imgpath='test')
        self.valid_course = {
            "name": "Russian",
            "description": "Russian course",
            "category": 1,
            "logo": "logo.jpg",
            "branches": [
                {
                    "latitude": "484654684165156",
                    "longitude": "846878787878787",
                    "address": "Ahunbaeva 47"
                }
            ],
            "contacts": [
                {
                    "type": 1,
                    "value": "+99678445154564645"
                }
            ]
        }

        self.invalid_course = {
        }

    def test_course_post_valid(self):
        response = client.post('/course/', self.valid_course, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_course_post_invalid(self):
        response = client.post('/course/', self.invalid_course, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class CourseTestDeleteSingle(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Programming', imgpath='test')
        self.course = Course.objects.create(name='English', description='test', category=self.category, logo='test')

    def test_course_delete_valid(self):
        url = reverse('CourseDetailUrl', kwargs={'pk': self.course.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_course_delete_invalid(self):
        url = reverse('CourseDetailUrl', kwargs={'pk': 30})
        response = client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
