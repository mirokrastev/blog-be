from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts import models
from accounts import serializers
from accounts import schemas


class LoginView(TokenObtainPairView):
    @schemas.LoginViewSchema.post
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterView(CreateAPIView):
    queryset = models.BaseUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = ()

    @schemas.RegisterViewSchema.post
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
