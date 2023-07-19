from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.serializers import TokenRefreshSerializer


class LoginViewSchema:
    @staticmethod
    def post(func):
        schema = swagger_auto_schema(
            responses={
                status.HTTP_201_CREATED: openapi.Response(
                    description='',
                    schema=TokenRefreshSerializer
                )
            }
        )

        return schema(func)


class RegisterViewSchema:
    @staticmethod
    def post(func):
        schema = swagger_auto_schema(
            responses={
                status.HTTP_201_CREATED: openapi.Response(
                    description='',
                    examples={
                        'application/json': {
                            'status': 'OK',
                        }
                    }
                )
            }
        )

        return schema(func)
