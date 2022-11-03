from django.test import TestCase

import random
import string

from .models import Camera
# Create your tests here.


class CameraModelTests(TestCase):

    def test_is_online_positive(self):
        test_cam = Camera(cam_name='testcam', ip='127.0.0.1')
        self.assertIs(test_cam.online(), True)

    def test_is_online_negative(self):
        test_cam = Camera(cam_name='testcam', ip='127.1.1.1')
        self.assertIs(test_cam.online(), False)

    def test_max_length(self):
        test_cam = Camera(cam_name=''.join(random.choice(string.ascii_letters) for i in range(50)), ip='255.255.255.255')

    def test_overflow_length(self):
        test_cam = Camera(cam_name=''.join(random.choice(string.ascii_letters) for i in range(52)), ip='255.255.255.2550')

    def test_null_length(self):
        test_cam = Camera(cam_name='', ip='')


