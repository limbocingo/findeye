from django.http.response import HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from user.models import User
from user.v2.utils import get_image, upload_image


class UserPfpViewSet(ViewSet):
    def retrieve(self, request: Request, pk: int):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'detail': 'Not found.'})

        image, format = get_image(user.picture)

        return HttpResponse(image, content_type='image/' + format)

    def upload(self, request: Request, pk: int):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)

        image, format, error = upload_image(
            user, 'picture', request.FILES.get('image'), resize=(128, 128))
        if error:
            return Response({'image': [
                error
            ]}, status=400)

        return HttpResponse(image, content_type="image/" + format)