from django.urls import re_path

from admin.views import Login, Panel

urlpatterns = [
    re_path(r'^/login/?$', Login.as_view()),
    re_path(r'^/panel/?$', Panel.as_view()),
]
