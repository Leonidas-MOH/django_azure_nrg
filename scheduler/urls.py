from django.urls import path
##from . import views
from . import viewsScheduler
from . import viewsTask
from . import viewsScheduledTask
from . import ViewSchedulerLog
from . import viewsTaskParam


urlpatterns = [
##    path('list/', views.MetricsDetailFiltered, name='list'),
##    path('add/', views.MetricsCreate.as_view(), name='add'),
##    path('edit/<int:pk>/', views.MetricsEdit.as_view(), name='edit'),
##    path('view/<int:pk>/', views.MetricView.as_view(), name='view'),

    path('schedulerlist/', viewsScheduler.DetailFiltered, name='schedulerlist'),
    path('scheduleradd/', viewsScheduler.Create.as_view(), name='scheduleradd'),
    path('scheduleredit/<int:pk>/', viewsScheduler.Edit.as_view(), name='scheduleredit'),
    path('schedulerview/<int:pk>/', viewsScheduler.View.as_view(), name='schedulerview'),

    path('scheduleloglist/', ViewSchedulerLog.DetailFiltered, name='scheduleloglist'),
    path('schedulelogadd/', ViewSchedulerLog.Create.as_view(), name='schedulelogadd'),
    path('schedulelogedit/<int:pk>/', ViewSchedulerLog.Edit.as_view(), name='schedulelogedit'),
    path('schedulelogview/<int:pk>/', ViewSchedulerLog.View.as_view(), name='schedulelogview'),

    path('tasklist/', viewsTask.DetailFiltered, name='tasklist'),
    path('taskadd/', viewsTask.Create.as_view(), name='taskadd'),
    path('taskedit/<int:pk>/', viewsTask.Edit.as_view(), name='taskedit'),
    path('taskview/<int:pk>/', viewsTask.View.as_view(), name='taskview'),

    path('scheduledtasklist/', viewsScheduledTask.DetailFiltered, name='scheduledtasklist'),
    path('scheduledtasadd/', viewsScheduledTask.Create.as_view(), name='scheduledtaskadd'),
    path('scheduledtasedit/<int:pk>/', viewsScheduledTask.Edit.as_view(), name='scheduledtaskedit'),
    path('scheduledtasview/<int:pk>/', viewsScheduledTask.View.as_view(), name='scheduledtaskview'),

    path('taskparamlist/', viewsTaskParam.DetailFiltered, name='taskparamlist'),
    path('taskparamadd/', viewsTaskParam.Create.as_view(), name='taskparamadd'),
    path('taskparamedit/<int:pk>/', viewsTaskParam.Edit.as_view(), name='taskparamedit'),
    path('taskparamview/<int:pk>/', viewsTaskParam.View.as_view(), name='taskparamview'),

##    path('scheduledtaskloglist/', viewsScheduledTaskLog.DetailFiltered, name='scheduledtaskloglist'),
##    path('scheduledtaslogview/<int:pk>/', viewsScheduledTaskLog.View.as_view(), name='scheduledtasklogview'),
    
    ]

