from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^subjects/$', views.SubjectListCreateView.as_view(), name='create_subjects'),
    url(r'^subjects/(?P<pk>[^/]+)/$', views.SubjectDetailView.as_view(), name='detail_subjects'),
    url(r'^colors/$', views.ColorListView.as_view(), name='list_colors')
]