from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    post_count = models.IntegerField(default=0)
    follower_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        swappable = 'AUTH_USER_MODEL'
