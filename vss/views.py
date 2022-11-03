from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Camera


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'vss/index.html'
    context_object_name = 'cameras'

    def get_queryset(self):
        return Camera.objects.all()


class AddCameraView(generic.ListView):
    model = Camera
    template_name = 'vss/add_camera.html'


class DetailsView(generic.ListView):
    model = Camera
    template_name = 'vss/details.html'
    context_object_name = 'camera'

    def get_queryset(self):
        pk = 1
        return Camera.objects.get(pk=pk)


def add_camera_action(request):
    #pk = request.POST['pk']
    cam_name = request.POST['cam_name']
    ip = request.POST['ip']
    new_cam = Camera(cam_name=cam_name,ip=ip)
    new_cam.save()
    return HttpResponseRedirect(reverse('vss:index'))


def delete_camera_action(request):
    cam = Camera.object.get(pk='something')
    cam.delete()
    return HttpResponseRedirect(reverse('vss:index'))