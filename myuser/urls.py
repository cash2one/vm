#encoding=utf-8
from django.conf.urls import patterns
from django.views.generic import TemplateView

import views_account
urlpatterns = patterns('',
	(r'^login/$', views_account.login_ajax),#登录页面
	(r'^logout/$', views_account.logout_ajax),#注销页面
)