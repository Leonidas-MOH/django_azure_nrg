from django.contrib import admin

# Register your models here.

from simple_history.admin import SimpleHistoryAdmin
from .models import Country

admin.site.register(Country, SimpleHistoryAdmin)
