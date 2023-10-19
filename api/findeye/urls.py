from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('api/v1/users', include('user.v1.urls')),
    re_path(r'^api/admin', include('admin.urls')),
]

urlpatterns += staticfiles_urlpatterns()
