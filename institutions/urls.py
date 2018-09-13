from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^types/$', views.InstitutionTypeListCreateView.as_view(), name='create_institution_types'),
    url(r'^types/(?P<pk>[^/]+)/$', views.InstitutionTypeDetailView.as_view(), name='detail_institution_types'),
    url(r'^$', views.InstitutionListView.as_view(), name='create_institutions'),
    url(r'^(?P<pk>[^/]+)/$', views.InstitutionDetailView.as_view(), name='detail_institutions'),
]