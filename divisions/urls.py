from django.conf.urls import url

from divisions import views

urlpatterns = [
    url(r'^levels/$', views.ClassLevelListCreateView.as_view(), name='create_class_levels'),
    url(r'^levels/(?P<pk>[^/]+)/$', views.ClassLevelDetailView.as_view(), name='detail_class_level'),
    url(r'^streams/$', views.StreamListCreateView.as_view(), name='create_streams'),
    url(r'^streams/(?P<pk>[^/]+)/$', views.StreamDetailView.as_view(), name='detail_streams'),
    url(r'^classes/$', views.ClassListCreateView.as_view(), name='create_classes'),
    url(r'^classes/(?P<pk>[^/]+)/$', views.ClassDetailView.as_view(), name='detail_classes'),
    url(r'^students/comments/$', views.StudentCommentListCreateView.as_view(), name='create_student_comments'),
    url(r'^students/comments/(?P<pk>[^/]+)/$', views.StudentCommentDetailView.as_view(),
        name='detail_student_comments'),
    url(r'^students/$', views.StudentListCreateView.as_view(), name='create_students'),
    url(r'^students/(?P<pk>[^/]+)/$', views.StudentDetailView.as_view(), name='detail_students'),
    url(r'^teachers/$', views.TeacherListCreateView.as_view(), name='create_teachers'),
    url(r'^teachers/(?P<pk>[^/]+)/$', views.TeacherDetailView.as_view(), name='detail_teachers'),
    url(r'^parents/$', views.ParentListCreateView.as_view(), name='create_parents'),
    url(r'^parents/(?P<pk>[^/]+)/$', views.ParentDetailView.as_view(), name='detail_parents'),
    url(r'^subjects/$', views.InstitutionSubjectListCreateView.as_view(), name='create_subjects'),
    url(r'^subjects/(?P<pk>[^/]+)/$', views.InstitutionSubjectDetailView.as_view(), name='detail_subjects'),
    url(r'^class_rooms/$', views.ClassRoomListCreateView.as_view(), name='create_class_rooms'),
    url(r'^class_rooms/(?P<pk>[^/]+)/$', views.ClassRoomDetailView.as_view(), name='detail_class_rooms'),
]