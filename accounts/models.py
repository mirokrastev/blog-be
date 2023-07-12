from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class BaseUser(BaseModel, AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("user")
        verbose_name_plural = _("users")
