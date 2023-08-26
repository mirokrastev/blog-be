from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField
from accounts.models import BaseUser
from base.models import BaseModel


class Category(BaseModel):
    title = models.CharField(_('title'), max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Article(BaseModel):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    content = RichTextField()
    categories = models.ManyToManyField(Category, blank=True, related_name='articles')
    authors = models.ManyToManyField(BaseUser, related_name='articles')
    # todo add visible_on_website bool

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
