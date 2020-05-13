from django.urls import path
from . import viewsMetrics
from . import viewsCategory
from . import viewsTables
from . import viewsFields

urlpatterns = [
    path('list/', viewsMetrics.DetailFiltered, name='list'),
    path('add/', viewsMetrics.Create.as_view(), name='add'),
    path('edit/<int:pk>/', viewsMetrics.Edit.as_view(), name='edit'),
    path('view/<int:pk>/', viewsMetrics.View.as_view(), name='view'),

    path('metricslist/', viewsMetrics.DetailFiltered, name='metricslist'),
    path('metricsadd/', viewsMetrics.Create.as_view(), name='metricsadd'),
    path('metricsedit/<int:pk>/', viewsMetrics.Edit.as_view(), name='metricsedit'),
    path('metricsview/<int:pk>/', viewsMetrics.View.as_view(), name='metricsview'),


    path('tableslist/', viewsTables.DetailFiltered, name='tableslist'),
    path('tablesadd/', viewsTables.Create.as_view(), name='tablesadd'),
    path('tablesedit/<int:pk>/', viewsTables.Edit.as_view(), name='tablesedit'),
    path('tablesview/<int:pk>/', viewsTables.View.as_view(), name='tablesview'),

    path('fieldslist/', viewsFields.DetailFiltered, name='fieldslist'),
    path('fieldsadd/', viewsFields.Create.as_view(), name='fieldsadd'),
    path('fieldsedit/<int:pk>/', viewsFields.Edit.as_view(), name='fieldsedit'),
    path('fieldsview/<int:pk>/', viewsFields.View.as_view(), name='fieldsview'),

    path('categorylist/', viewsCategory.DetailFiltered, name='categorylist'),
    path('categoryadd/', viewsCategory.Create.as_view(), name='categoryadd'),
    path('categoryedit/<int:pk>/', viewsCategory.Edit.as_view(), name='categoryedit'),
    path('categoryview/<int:pk>/', viewsCategory.View.as_view(), name='categoryview'),

    
    ]

