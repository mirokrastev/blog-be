from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, swagger_serializer_method
from rest_framework import status


class ArticleSchema:
    @staticmethod
    def list(func):
        schema = swagger_auto_schema(
            responses={
                status.HTTP_200_OK: openapi.Response(description='')
            }
        )
        return schema(func)
