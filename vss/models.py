from django.db import models
from ping3 import ping


# Create your models here.

class Camera(models.Model):

    def __str__(self):
        return self.cam_name

    def online(self):
        if ping(self.ip):
            return True
        else:
            return False

    cam_name = models.CharField(max_length=50)
    ip = models.GenericIPAddressField(protocol='IPv4')
