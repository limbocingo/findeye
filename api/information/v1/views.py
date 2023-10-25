"""
Views of Information application.

[version: v1]
[author: mrcingo]
"""

from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from user.v2.utils import get_image, upload_image

from information.models import *
from information.v1.serializers import *


class BadgeViewSet(ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class BadgeIconViewSet(ViewSet):
    def retrieve(self, request: Request, pk: int):
        try:
            badge = Badge.objects.get(pk=pk)
        except Badge.DoesNotExist:
            return Response({'detail': 'Not found.'})

        image, format = get_image(badge.picture)

        return HttpResponse(image, content_type='image/' + format)

    def upload(self, request: Request, pk: int):
        try:
            user = Badge.objects.get(pk=pk)
        except Badge.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)

        image, format, error = upload_image(
            user, 'icon', request.FILES.get('image'), resize=(128, 128))
        if error:
            return Response({'image': [
                error
            ]}, status=400)

        return HttpResponse(image, content_type="image/" + format)
