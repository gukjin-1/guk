from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#CASCADE 관련된거 삭제
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True) ##경로지정옵션
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)