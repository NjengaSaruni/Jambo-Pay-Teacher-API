from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

v1_urls = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^library/', include('library.urls', namespace='library')),
    url(r'^divisions/', include('divisions.urls', namespace='divisions')),
    url(r'^common/', include('common.urls', namespace='common')),
    url(r'^exams/', include('exams.urls', namespace='exams')),
    url(r'^uploads/', include('uploads.urls', namespace='uploads')),
    url(r'^intelligence/', include('intelligence.urls', namespace='intelligence')),
    url(r'^institutions/', include('institutions.urls', namespace='institutions')),
    url(r'^messaging/', include('messaging.urls', namespace='messaging'))
]

urlpatterns = [
    url(r'^v1/', include(v1_urls, namespace='v1')),
]
