#encoding=utf-8
from django.conf.urls import patterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name="website/query_data_daily.html")), #首页, 分日页面
    (r'^query_data_daily$', TemplateView.as_view(template_name="website/query_data_daily.html")), #分日页面
    (r'^query_data_hourly$', TemplateView.as_view(template_name="website/query_data_hourly.html")), #分时页面
    (r'^visual_data_daily$', TemplateView.as_view(template_name="website/visual_data_daily.html")), #分日曲线
    (r'^visual_data_hourly$', TemplateView.as_view(template_name="website/visual_data_hourly.html")), #分时曲线
    (r'^node_all$', TemplateView.as_view(template_name="website/node_all.html")), #节点全景
    (r'^node_manage$', TemplateView.as_view(template_name="website/node_manage.html")), #节点管理
)