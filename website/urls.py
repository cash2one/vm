#encoding=utf-8

from django.conf.urls import patterns
from django.views.generic import TemplateView
from website.views import getDataHourly

import views_page
urlpatterns = patterns('',
    (r'^$', views_page.index), #首页, 分日页面
    (r'^query_data_daily$', views_page.query_data_daily), #分日页面
    (r'^query_data_hourly$', views_page.query_data_hourly), #分时页面
    (r'^visual_data_daily$', views_page.visual_data_daily), #分日曲线
    (r'^visual_data_hourly$', views_page.visual_data_hourly), #分时曲线
    (r'^node_all$', views_page.node_all), #节点全景
    (r'^node_manage$', views_page.node_manage), #节点管理
)

import views_account
urlpatterns += patterns('',
        (r'^login_page/$', TemplateView.as_view(template_name="website/login.html")),#登录页面
        (r'^login/$', views_account.login_ajax),#登录函数
        (r'^logout/$', views_account.logout_ajax),#注销函数
)

import views
urlpatterns += patterns('',
    (r'^node_all_location$', views.node_all),
    (r'^get_data_hourly$', views.getDataHourly),
    (r'^get_node_desc$', views.getNodeDesc), 
)

import views_data_query
urlpatterns += patterns('',
    (r'^query_data_daily_search$', views_data_query.search_daily),
)
