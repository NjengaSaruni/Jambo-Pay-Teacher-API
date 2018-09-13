from django.conf.urls import url
from library import views

urlpatterns = [
    url(r'^books/$', views.BookListCreateView.as_view(), name='create_books'),
    url(r'^books/(?P<pk>[^/]+)/$', views.BookDetailView.as_view(), name='detail_books'),
]