# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Myuser(AbstractUser):
    nickname = models.CharField('昵称', max_length=15, blank=True)
    avatar = ProcessedImageField(upload_to='avatar',
                                 default='/media/avatar/default.png',
                                 verbose_name='头像',
                                 processors=[ResizeToFill(80, 80)]
                                 )

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username