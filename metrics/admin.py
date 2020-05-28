from django.contrib import admin

# Register your models here.

from simple_history.admin import SimpleHistoryAdmin

from .models import Metric, FieldParam, TableParam, MetricCategory

admin.site.register(Metric, SimpleHistoryAdmin)
admin.site.register(FieldParam, SimpleHistoryAdmin)
admin.site.register(TableParam, SimpleHistoryAdmin)
admin.site.register(MetricCategory, SimpleHistoryAdmin)
