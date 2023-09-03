from rest_framework import mixins, viewsets

from articles import serializers
from articles import models


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = []


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()
    permission_classes = []
