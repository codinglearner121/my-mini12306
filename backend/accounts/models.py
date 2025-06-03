# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, verbose_name='姓名')
    id_card = models.CharField(max_length=18, unique=True, verbose_name='身份证号')
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'id_card']
