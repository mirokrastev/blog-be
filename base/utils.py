from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.views import exception_handler
from rest_framework import exceptions, serializers


def custom_exception_handler(exc, context):
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(serializers.as_serializer_error(exc))

    response = exception_handler(exc, context)
    return response


def create_serializer_class(name, fields):
    return type(name, (serializers.Serializer,), fields)


def inline_serializer(*, fields, data=None, **kwargs):
    serializer_class = create_serializer_class(name="inline_serializer", fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)


class InputOutputField(serializers.Field):
    def __init__(
        self,
        input: serializers.Serializer | serializers.Field,
        output: serializers.Serializer | serializers.Field,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.input = input
        self.output = output

    def to_internal_value(self, data):
        return self.input.to_internal_value(data)

    def to_representation(self, value):
        return self.output.to_representation(value)
