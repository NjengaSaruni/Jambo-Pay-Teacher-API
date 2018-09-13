from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^images/$', views.ImageListCreateView.as_view(), name='create_image'),
    url(r'^images/(?P<pk>[^/]+)/$', views.ImageDetailView.as_view(), name='detail_image'),
    url(r'^files/$', views.FileListCreateView.as_view(), name='create_file'),
    url(r'^files/(?P<pk>[^/]+)/$', views.FileDetailView.as_view(), name='detail_file'),
]

