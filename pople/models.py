from django.db import models
# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # groups and user_permissions uchun related_name qo'shish
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Bu yerda `customuser_set` ni mos ravishda o'zgartiring
        blank=True,
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Bu yerda ham `customuser_set` ni mos ravishda o'zgartiring
        blank=True,
        related_query_name='customuser'
    )
