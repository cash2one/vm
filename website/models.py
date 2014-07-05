#encoding=utf-8
from django.db import models
from django.core.exceptions import ValidationError

def validate_sim_char_num(value):
    if len(value) != 11:
        raise ValidationError(u'SIM必须为11位')
        
def format_minute_data_identity(data, type):
    time = data.data_time
    return str(type) + '+++' + str(data.node.name_id) + '+++' + str(time.year) + str(time.month) + str(time.day) + ' ' + str(time.hour) + ':' + str(time.minute)
    
def format_daily_data_identity(data, type):
    time = data.data_time
    return str(type) + '+++' + str(data.node.name_id) + '+++' + str(time.year) + str(time.month) + str(time.day)

class Node(models.Model):
    company = models.ForeignKey('myuser.Company', verbose_name='公司名称')
    name_id = models.IntegerField(unique=True, verbose_name='节点ID')
    alias = models.CharField(max_length=20, verbose_name='别名')
    net_name = models.CharField(max_length=20, unique=True, verbose_name='节点网')
    desc = models.CharField(max_length=40, verbose_name='描述')
    max_voltage = models.IntegerField(verbose_name='电压上限')
    min_voltage = models.IntegerField(verbose_name='电压下限')
    max_current = models.IntegerField(verbose_name='电流上限')
    min_current = models.IntegerField(verbose_name='电流下限')
    latitude = models.CharField(max_length=20, verbose_name='纬度')
    longitude = models.CharField(max_length=20, verbose_name='经度')
    sim_id = models.CharField(max_length=11, validators=[validate_sim_char_num], verbose_name='SIM')
    expire_time = models.DateTimeField(verbose_name='失效时间')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    def __unicode__(self):
        return self.name_id
    
    class Meta:
        verbose_name = '节点'
        verbose_name_plural = '节点'
    
class CMinuteData(models.Model):
    node = models.ForeignKey('Node', verbose_name='节点')
    potential = models.IntegerField(default=0, verbose_name='电位')
    power_voltage = models.IntegerField(default=0, verbose_name='电源电压')
    data_time = models.DateTimeField(verbose_name='数据时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    def __unicode__(self):
        return format_minute_data_identity(self, 'C')

class HMinuteData(models.Model):
    node = models.ForeignKey('Node', verbose_name='节点')
    potential = models.IntegerField(default=0, verbose_name='参比电位')
    voltage = models.IntegerField(default=0, verbose_name='输出电压')
    current = models.IntegerField(default=0, verbose_name='输出电流')
    data_time = models.DateTimeField(verbose_name='数据时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    def __unicode__(self):
        return format_minute_data_identity(self, 'H')

class CDailyData(models.Model):
    node = models.ForeignKey('Node', verbose_name='节点')
    max_voltage = models.IntegerField(default=0, verbose_name='最大电压')
    min_voltage = models.IntegerField(default=0, verbose_name='最小电压')
    avg_voltage = models.IntegerField(default=0, verbose_name='平均电压')
    mse_voltage = models.IntegerField(default=0, verbose_name='电压均方差')
    voltage_failure_times = models.IntegerField(default=0, verbose_name='电压失效次数')
    voltage_exception_times = models.IntegerField(default=0, verbose_name='电压异常次数')
    voltage_exception_period = models.IntegerField(default=0, verbose_name='电压异常时间')
    data_time = models.DateField(verbose_name='数据时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    def __unicode__(self):
        return format_daily_data_identity(self, 'C')
        
class HDailyData(models.Model):
    node = models.ForeignKey('Node', verbose_name='节点')
    max_voltage = models.IntegerField(default=0, verbose_name='最大电压')
    min_voltage = models.IntegerField(default=0, verbose_name='最小电压')
    avg_voltage = models.IntegerField(default=0, verbose_name='平均电压')
    mse_voltage = models.IntegerField(default=0, verbose_name='电压均方差')
    voltage_failure_times = models.IntegerField(default=0, verbose_name='电压失效次数')
    voltage_exception_times = models.IntegerField(default=0, verbose_name='电压异常次数')
    voltage_exception_period = models.IntegerField(default=0, verbose_name='电压异常时间')
    max_protential = models.IntegerField(default=0, verbose_name='最大电位')
    min_protential = models.IntegerField(default=0, verbose_name='最小电位')
    avg_protential = models.IntegerField(default=0, verbose_name='平均电位')
    mse_protential = models.IntegerField(default=0, verbose_name='电位均方差')
    protential_failure_times = models.IntegerField(default=0, verbose_name='电位失效次数')
    protential_exception_times = models.IntegerField(default=0, verbose_name='电位异常次数')
    protential_exception_period = models.IntegerField(default=0, verbose_name='电位异常时间')
    max_current = models.IntegerField(default=0, verbose_name='最大电流')
    min_current = models.IntegerField(default=0, verbose_name='最小电流')
    avg_current = models.IntegerField(default=0, verbose_name='平均电流')
    mse_current = models.IntegerField(default=0, verbose_name='电流均方差')
    current_failure_times = models.IntegerField(default=0, verbose_name='电流失效次数')
    current_exception_times = models.IntegerField(default=0, verbose_name='电流异常次数')
    current_exception_period = models.IntegerField(default=0, verbose_name='电流异常时间')
    data_time = models.DateField(verbose_name='数据时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    def __unicode__(self):
        return format_daily_data_identity(self, 'H')

class AlertParam(models.Model):
    node = models.ForeignKey('Node', unique=True, verbose_name='节点')
    user = models.ForeignKey('myuser.MyUser', unique=True, verbose_name='用户')
    invalid_times = models.IntegerField(default=0, verbose_name='失效次数')
    exception_times = models.IntegerField(default=0, verbose_name='异常次数')
    mse = models.FloatField(default=0, verbose_name='均方差')
    power_voltage = models.FloatField(default=0, verbose_name='电池电压')
    no_data_days = models.IntegerField(default=0, verbose_name='无数据天')
    recharge_expire_days = models.IntegerField(default=0, verbose_name='充值到期天数')
    email = models.CharField(max_length=40, verbose_name='通知邮箱')
    
    def __unicode__(self):
        return str(node.name) + '+++' + str(user.name)
        
    class Meta:
        verbose_name = '报警关联'
        verbose_name_plural = '报警关联'
    
    