from django.urls import path
from . import viewsCountry
#from . import views

urlpatterns = [
    path('countrylist/', viewsCountry.DetailFiltered, name='countrylist'),
    path('countryadd/', viewsCountry.Create.as_view(), name='countryadd'),
    path('countryedit/<int:pk>/', viewsCountry.Edit.as_view(), name='countryedit'),
    path('countryview/<int:pk>/', viewsCountry.View.as_view(), name='countryview'),
    
##    path('table', views.Home, name='table'),
##    path('table0', views.Home0, name='table0'),
##    path('add/', views.CountryCreate.as_view(), name='add'),
##    path('view/<int:pk>/', views.CountryView.as_view(), name='view'),
##    path('edit/<int:pk>/', views.CountryEdit.as_view(), name='edit'),
##    path('display/', views.CountryDetailFiltered, name='display'),
##    path('list/', views.CountryDetailFiltered, name='list'),
    ]

