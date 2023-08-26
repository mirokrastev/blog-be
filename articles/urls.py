from django.urls import path, include
from rest_framework import routers

from articles import views

app_name = 'articles'

router = routers.SimpleRouter()
router.register('categories', views.CategoryViewSet)
router.register('articles', views.ArticleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
