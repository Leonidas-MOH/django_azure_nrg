from django.contrib import admin

# Register your models here.

from simple_history.admin import SimpleHistoryAdmin
from .models import MeteoDetNew, SpotDetNew, SeecaoDet
admin.site.register(MeteoDetNew, SimpleHistoryAdmin)
admin.site.register(SpotDetNew, SimpleHistoryAdmin)
admin.site.register(SeecaoDet, SimpleHistoryAdmin)
