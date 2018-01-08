from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """
    User:
        username: 아이디
        password: 비밀번호
        email: 이메일
        first_name:
        last_name:
        groups
        user_permissions
        is_staff
        is_active
        is_superuser
        last_login
        date_joined
    user_num:
    user_phone:
    level:
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=10)
    user_num = models.IntegerField()
    user_phone = models.CharField(max_length=20)
    level = models.PositiveSmallIntegerField(default=0)
    signup_date = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name.encode('utf8')