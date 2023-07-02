
from django.test import TestCase
from django.urls import reverse
from onlinecourse.models import *



# Create your tests here.

class CourseDetailViewTest(TestCase):
    def setup(self):
       
        self.course=Course.objects.get(id=1)

    def test_detail(self):
        response = self.client.get(reverse('onlier_course_details', self.course))     
        # url= reverse('onlinecourse:course_details')
        # response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response.content,status_code=200)

