from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^account_types/$', views.AccountTypeListCreateView.as_view(), name='create_account_types'),
    url(r'^account_types/(?P<pk>[^/]+)/$', views.AccountTypeDetailView.as_view(), name='detail_account_types'),
    url(r'^profiles/$', views.UserProfileListCreateView.as_view(), name='create_user_profiles'),
    url(r'^profiles/(?P<pk>[^/]+)/$', views.UserProfileDetailView.as_view(), name='detail_user_profiles'),
    url(r'^join_requests/$', views.InstitutionJoinRequestListCreateView.as_view(),
        name='create_institution_join_requests'),
    url(r'^join_requests/(?P<pk>[^/]+)/$', views.InstitutionJoinRequestDetailView.as_view(),
        name='detail_institution_join_requests'),
    url(r'^$', views.UserListView.as_view(), name='list_users'),
    url(r'^create/$', views.UserCreateView.as_view(), name='create_users'),
    url(r'^(?P<pk>[^/]+)/$', views.UserDetailView.as_view(), name='detail_users'),
]