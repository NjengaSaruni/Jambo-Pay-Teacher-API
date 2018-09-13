from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^class_subjects/$', views.ClassSubjectPredictionListView.as_view(), name='create_class_subject_predictions'),
    url(r'^class_subjects/(?P<pk>[^/]+)/$', views.ClassSubjectPredictionDetailView.as_view(),
        name='detail_class_subject_predictions'),
    url(r'^students/$', views.StudentPredictionListView.as_view(), name='create_student_predictions'),
    url(r'^students/(?P<pk>[^/]+)/$', views.StudentPredictionDetailView.as_view(), name='detail_student_predictions'),
]