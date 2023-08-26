from rest_framework import serializers

from accounts.models import BaseUser
from articles import models
from base.utils import inline_serializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title')


class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    categories_ids = serializers.PrimaryKeyRelatedField(
        queryset=models.Category.objects.all(),
        source='categories',
        many=True,
        write_only=True
    )

    authors = inline_serializer(fields={
        'id': serializers.SlugField(),
        'username': serializers.CharField(),
        'first_name': serializers.CharField(),
        'last_name': serializers.CharField(),
    },
        many=True,
        read_only=True
    )
    authors_ids = serializers.PrimaryKeyRelatedField(
        queryset=BaseUser.objects.filter(is_staff=True),
        source='authors',
        many=True,
        write_only=True
    )

    class Meta:
        model = models.Article
        fields = ('id', 'slug', 'content', 'categories', 'categories_ids', 'authors', 'authors_ids')
