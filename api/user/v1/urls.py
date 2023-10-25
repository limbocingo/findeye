"""
Urls for the User views.

[version: 1v]
"""

from django.urls import re_path

from user.v1.views import UserViewSet

urlpatterns = [
    re_path(r'^/?$', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    re_path(r'^/(?P<discord_id>\w+)/?$', UserViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),
]
