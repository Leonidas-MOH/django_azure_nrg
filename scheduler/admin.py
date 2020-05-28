from django.contrib import admin

# Register your models here.

from simple_history.admin import SimpleHistoryAdmin
from .models import ScheduledTask, Scheduler, Task, TaskParam

admin.site.register(ScheduledTask, SimpleHistoryAdmin)
admin.site.register(Scheduler, SimpleHistoryAdmin)
admin.site.register(Task, SimpleHistoryAdmin)
admin.site.register(TaskParam, SimpleHistoryAdmin)
