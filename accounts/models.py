import uuid

from django.db import models
from django.utils.timezone import now

USER_SEX_CHOICE = (
    ('m', '男'),
    ('w', '女'),
)


# Create your models here.
class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField('用户名', max_length=200)
    tel_phone = models.CharField('手机号', max_length=100, null=True)
    wxusermodel = models.ForeignKey('accounts.WxUserModel', verbose_name='微信用户', on_delete=models.CASCADE, null=True,
                                    default=None)
    sex = models.CharField('性别', max_length=1, choices=USER_SEX_CHOICE, default='m')
    headimage = models.CharField('头像', max_length=1000, null=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.__str__()

    class Meta:
        ordering = ['-created_time']
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'


class WxUserModel(models.Model):
    openid = models.CharField('openid', max_length=200)
    matedata = models.CharField('matedata', max_length=2000)
    headimage = models.CharField('头像', max_length=1000, null=True)
    access_token = models.CharField("access_token", max_length=300, null=True)
    refresh_token = models.CharField("refresh_token", max_length=300, null=True)
    expires_in = models.IntegerField("expires_in", null=True)
    last_login_time = models.DateTimeField("最后登录时间", default=now)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)

    def __str__(self):
        return self.openid

    class Meta:
        ordering = ['-created_time']
        verbose_name = "微信用户"
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'
