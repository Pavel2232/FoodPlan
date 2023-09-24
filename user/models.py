from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions',
                                              related_name='customuser_set')


    EMAIL_FIELD = 'email'