from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^post_comments/$', views.PostCommentListCreateView.as_view(), name='create_post_comments'),
    url(r'^post_comments/(?P<pk>[^/]+)/$', views.PostCommentDetailView.as_view(), name='detail_post_comments'),
    url(r'^posts/$', views.PostListCreateView.as_view(), name='create_posts'),
    url(r'^posts/(?P<pk>[^/]+)/$', views.PostDetailView.as_view(), name='detail_posts'),
]