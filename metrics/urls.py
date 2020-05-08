from django.urls import path
from . import views
from . import viewsCategory
from . import viewsTables
from . import viewsFields

urlpatterns = [
    path('list/', views.MetricsDetailFiltered, name='list'),
    path('add/', views.MetricsCreate.as_view(), name='add'),
    path('edit/<int:pk>/', views.MetricsEdit.as_view(), name='edit'),
    path('view/<int:pk>/', views.MetricView.as_view(), name='view'),

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

