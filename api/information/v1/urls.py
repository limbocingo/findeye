"""
Urls patterns of Information application.

[version: v1]
[author: mrcingo]
"""


from django.urls import re_path

from information.v1.views import *

urlpatterns = [
    re_path(r'^/badges/?$', BadgeViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    re_path(r'^badges/(?P<pk>\w+)/?$', BadgeViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),

    re_path(r'^/skills/?$', SkillViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    re_path(r'^/skills/(?P<pk>\w+)/?$', SkillViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),

    re_path(r'^/languages/?$', LanguageViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    re_path(r'^/languages/(?P<pk>\w+)/?$', LanguageViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),
]
