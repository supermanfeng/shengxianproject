from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
      UserProfile并没有去替换系统用户,所以想去替换就在settings里面设置AUTH_USER_MODEL

    """

    name = models.CharField(max_length=32, null=True, blank=True, verbose_name="姓名")
    birth = models.DateField(null=True, blank=True, verbose_name='出生年月')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='female',
                              verbose_name='性别')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.username


class VerifyCode(models.Model):
    """
    短信验证码

    """

    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.code

