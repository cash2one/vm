#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='公司名称')
    address = models.TextField(blank=True, verbose_name='公司地址')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '公司'
        verbose_name_plural = '公司'
    
class MyUser(models.Model):
    GENDER = (
        ('male', '男'),
        ('female', '女'),
    )
    STATUS = (
        ('disabled', '禁用'),
        ('enabled', '可用'),
    )
    user = models.OneToOneField(User, related_name='my_user', verbose_name=u'用户基本信息')
    name = models.CharField(max_length=40, verbose_name=u'姓名')
    login_id = models.CharField(max_length=40, verbose_name=u'登录号')
    gender = models.CharField(max_length=40, choices=GENDER, verbose_name=u'性别')
    status = models.CharField(max_length=40, choices=STATUS, verbose_name=u'使用状态')
    identity = models.CharField(max_length=40, blank=True, verbose_name=u'身份证号')
    birthday = models.DateField(blank=True, verbose_name=u'出生日期')
    phone = models.CharField(max_length=40, blank=True, verbose_name=u'电话号码')
    cellphone = models.CharField(max_length=40, blank=True, verbose_name=u'手机号')
    mail = models.CharField(max_length=40, blank=True, verbose_name=u'邮箱')
    position = models.CharField(max_length=40, blank=True, verbose_name=u'职务')
    company = models.ForeignKey(Company, blank=True, verbose_name=u'公司')
    created_user = models.ForeignKey('self', related_name='+', blank=True, verbose_name=u'创建人')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    last_modified_user = models.ForeignKey('self', related_name='+', blank=True, verbose_name=u'修改人')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name=u'最后修改时间')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
    
