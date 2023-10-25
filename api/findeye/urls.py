from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # version: v1
    path('api/v1/users', include('user.v1.urls')),
    path('api/v1/information', include('information.v1.urls')),

    # admin panel
    path('api/admin', include('admin.urls')),
]

urlpatterns += staticfiles_urlpatterns()
