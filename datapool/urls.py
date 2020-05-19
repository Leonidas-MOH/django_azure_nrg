from django.urls import path
##from . import views

from . import viewsDailyPtr
from . import viewsFundamentalsMFv
from . import viewsFundamentalsMOv
from . import viewsFundamentalsMSv
from . import viewsFundamentalsWAv
from . import viewsFundamentalsWFv
from . import viewsFundamentalsWHv
from . import viewsSpotPrices
from . import viewsUpdateMC
from . import viewsView1
from . import viewsDiff

urlpatterns = [
##    path('list/', views.MetricsDetailFiltered, name='list'),
##    path('add/', views.MetricsCreate.as_view(), name='add'),
##    path('edit/<int:pk>/', views.MetricsEdit.as_view(), name='edit'),
##    path('view/<int:pk>/', views.MetricView.as_view(), name='view'),

    path('dailyptrlist/', viewsDailyPtr.DetailFiltered, name='dailyptrlist'),
    path('dailyptrview/<int:pk>/', viewsDailyPtr.View.as_view(), name='dailyptrview'),

    path('fundamentalsMFvlist/', viewsFundamentalsMFv.DetailFiltered, name='fundamentalsMFvlist'),
    path('fundamentalsMFvview/<int:pk>/', viewsFundamentalsMFv.View.as_view(), name='fundamentalsMFvview'),

    path('fundamentalsMOvlist/', viewsFundamentalsMOv.DetailFiltered, name='fundamentalsMOvlist'),
    path('fundamentalsMOvview/<int:pk>/', viewsFundamentalsMOv.View.as_view(), name='fundamentalsMOvview'),

    path('fundamentalsMSvlist/', viewsFundamentalsMSv.DetailFiltered, name='fundamentalsMSvlist'),
    path('fundamentalsMSvview/<int:pk>/', viewsFundamentalsMSv.View.as_view(), name='fundamentalsMSvview'),

    path('fundamentalsWAvlist/', viewsFundamentalsWAv.DetailFiltered, name='fundamentalsWAvlist'),
    path('fundamentalsWAvview/<int:pk>/', viewsFundamentalsWAv.View.as_view(), name='fundamentalsWAvview'),

    path('fundamentalsWFvlist/', viewsFundamentalsWFv.DetailFiltered, name='fundamentalsWFvlist'),
    path('fundamentalsWFvview/<int:pk>/', viewsFundamentalsWFv.View.as_view(), name='fundamentalsWFvview'),

    path('fundamentalsWHvlist/', viewsFundamentalsWHv.DetailFiltered, name='fundamentalsWHvlist'),
    path('fundamentalsWHvview/<int:pk>/', viewsFundamentalsWHv.View.as_view(), name='fundamentalsWHvview'),

    path('spotpriceslist/', viewsSpotPrices.DetailFiltered, name='spotpriceslist'),
    path('spotpricesview/<int:pk>/', viewsSpotPrices.View.as_view(), name='spotpricesview'),

    path('updatedmclist/', viewsUpdateMC.DetailFiltered, name='updatedmclist'),
    path('updatedmcview/<int:pk>/', viewsUpdateMC.View.as_view(), name='updatedmcview'),

    path('view1list/', viewsView1.DetailFiltered, name='view1list'),
    path('view1view/<int:pk>/', viewsView1.View.as_view(), name='view1view'),

    path('viewdiff/', viewsDiff.get_name, name='viewdiff'),
    path('viewdiff0/<int:pk>/', viewsDiff.DetailFiltered, name='viewdiff0'),
    
    ]

