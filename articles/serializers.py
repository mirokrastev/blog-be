from rest_framework import serializers

from accounts.models import BaseUser
from articles import models
from base.utils import inline_serializer, InputOutputField


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title')


class ArticleSerializer(serializers.ModelSerializer):
    categories = InputOutputField(
        input=serializers.PrimaryKeyRelatedField(
            queryset=models.Category.objects.all(),
            many=True
        ),
        output=CategorySerializer(many=True)
    )
    authors = InputOutputField(
        input=serializers.PrimaryKeyRelatedField(
            queryset=BaseUser.objects.filter(is_staff=True),
            many=True
        ),
        output=inline_serializer(fields={
            'id': serializers.SlugField(),
            'username': serializers.CharField(),
            'first_name': serializers.CharField(),
            'last_name': serializers.CharField(),
        }, many=True)
    )

    class Meta:
        model = models.Article
        fields = ('id', 'slug', 'content', 'categories', 'authors')
