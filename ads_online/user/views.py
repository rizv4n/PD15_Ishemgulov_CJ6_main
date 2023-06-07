from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from user.models import User


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class UserUploadView(UpdateView):
    model = User

    fields = ['username', 'image']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "username": self.object.username,
            "image": self.object.image.url,
        })
