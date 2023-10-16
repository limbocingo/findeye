from django.urls import re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    re_path(r'^api/v1/users/', include('user.v1.urls')),
]

urlpatterns += staticfiles_urlpatterns()
