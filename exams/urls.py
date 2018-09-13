from django.conf.urls import url
from exams import views

urlpatterns = [
    url(r'^papers/$', views.ExamPaperListCreateView.as_view(), name='create_exam_papers'),
    url(r'^papers/(?P<pk>[^/]+)/$', views.ExamPaperDetailView.as_view(), name='detail_exam_papers'),
    url(r'^results/$', views.ClassExamResultListCreateView.as_view(), name='create_exam_results'),
    url(r'^results/(?P<pk>[^/]+)/$', views.ClassExamResultDetailView.as_view(), name='detail_exam_results'),
    url(r'^grades/$', views.GradeListCreateView.as_view(), name='create_grades'),
    url(r'^grades/(?P<pk>[^/]+)/$', views.GradeDetailView.as_view(), name='detail_grades'),
    url(r'^student_paper_performances/$', views.StudentPaperPerformanceListView.as_view(),
        name='create_student_paper_performances'),
    url(r'^student_paper_performances/(?P<pk>[^/]+)/$', views.StudentPaperPerformanceDetailView.as_view(),
        name='detail_student_paper_performances'),
    url(r'^class_paper_performances/$', views.ClassPaperPerformanceListView.as_view(),
        name='create_class_paper_performances'),
    url(r'^class_paper_performances/(?P<pk>[^/]+)/$', views.ClassPaperPerformanceDetailView.as_view(),
        name='detail_class_paper_performances'),
    url(r'^$', views.ExamListCreateView.as_view(), name='create_exams'),
    url(r'^(?P<pk>[^/]+)/$', views.ExamDetailView.as_view(), name='detail_exams'),
]