from django.urls import include, re_path
from . import views

urlpatterns = [
    #Home page
    re_path(r'^$', views.launch_detail, name='launcher_object'),
]