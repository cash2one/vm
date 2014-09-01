from django.contrib import admin

from website.models import *

admin.site.register(Node)
admin.site.register(AlertParam)


admin.site.register(CMinuteData)
admin.site.register(CDailyData)
