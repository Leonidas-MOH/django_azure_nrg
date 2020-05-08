from django.urls import path
##from . import views
from . import viewsWattSight
from . import viewsMeteo
from . import viewsSeecao

urlpatterns = [
##    path('list/', views.MetricsDetailFiltered, name='list'),
##    path('add/', views.MetricsCreate.as_view(), name='add'),
##    path('edit/<int:pk>/', views.MetricsEdit.as_view(), name='edit'),
##    path('view/<int:pk>/', views.MetricView.as_view(), name='view'),

    path('wattsightlist/', viewsWattSight.DetailFiltered, name='wattsightlist'),
    path('wattsightadd/', viewsWattSight.Create.as_view(), name='wattsightadd'),
    path('wattsightedit/<int:pk>/', viewsWattSight.Edit.as_view(), name='wattsightedit'),
    path('wattsightview/<int:pk>/', viewsWattSight.View.as_view(), name='wattsightview'),

    path('meteolist/', viewsMeteo.DetailFiltered, name='meteolist'),
    path('meteoadd/', viewsMeteo.Create.as_view(), name='meteoadd'),
    path('meteoedit/<int:pk>/', viewsMeteo.Edit.as_view(), name='meteoedit'),
    path('meteoview/<int:pk>/', viewsMeteo.View.as_view(), name='meteoview'),

    path('seecaolist/', viewsSeecao.DetailFiltered, name='seecaolist'),
    path('seecaoadd/', viewsSeecao.Create.as_view(), name='seecaoadd'),
    path('seecaoedit/<int:pk>/', viewsSeecao.Edit.as_view(), name='seecaoedit'),
    path('seecaoview/<int:pk>/', viewsSeecao.View.as_view(), name='seecaoview'),

##    path('fieldslist/', viewsFields.DetailFiltered, name='fieldslist'),
##    path('fieldsadd/', viewsFields.Create.as_view(), name='fieldsadd'),
##    path('fieldsedit/<int:pk>/', viewsFields.Edit.as_view(), name='fieldsedit'),
##    path('fieldsview/<int:pk>/', viewsFields.View.as_view(), name='fieldsview'),
##
##    path('categorylist/', viewsCategory.DetailFiltered, name='categorylist'),
##    path('categoryadd/', viewsCategory.Create.as_view(), name='categoryadd'),
##    path('categoryedit/<int:pk>/', viewsCategory.Edit.as_view(), name='categoryedit'),
##    path('categoryview/<int:pk>/', viewsCategory.View.as_view(), name='categoryview'),

    
    ]

