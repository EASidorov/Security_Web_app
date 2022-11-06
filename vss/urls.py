from django.urls import include, path

from . import views

app_name = 'vss'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_camera/', views.AddCameraView.as_view(), name='add_camera'),
    path('add_camera', views.add_camera_action, name='add_camera_action'),
    path('<int:pk>/cc/', views.change_camera_action, name='change_camera_action'),
    path('<int:pk>/dc/', views.delete_camera_action, name='delete_camera_action'),
    path('<int:pk>', views.DetailsView.as_view(), name='details')
]
