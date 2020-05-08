from django.db import models
from django.urls import reverse
from metrics.models   import *
from countries.models import *

class MeteoDetNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    metric_id = models.ForeignKey(Metric, models.DO_NOTHING, db_column='Metric_id')  # Field name made lowercase.
    country_id = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_id')  # Field name made lowercase.
    ftppath = models.CharField(db_column='FtpPath', max_length=255)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=120)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    tableto = models.CharField(db_column='TableTo', max_length=50)  # Field name made lowercase.
    fieldto = models.CharField(db_column='FieldTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insertminutes = models.IntegerField(db_column='InsertMinutes', blank=True, null=True)  # Field name made lowercase.
    daybefore = models.BooleanField(db_column='DayBefore')  # Field name made lowercase.
    dayafter = models.BooleanField(db_column='DayAfter')  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    timefrom = models.TimeField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.
    timeselection = models.TimeField(db_column='TimeSelection', blank=True, null=True)  # Field name made lowercase.
    headerrow = models.IntegerField(db_column='HeaderRow', blank=True, null=True)  # Field name made lowercase.
    usetimeframe = models.BooleanField(db_column='UseTimeFrame', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Meteo_Det_New'

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('fetchparams:meteodetlist')        


class SpotDetNew(models.Model):
    id = models.AutoField(primary_key=True)    
    curvesnameprice = models.CharField(db_column='CurvesNamePrice', max_length=150)  # Field name made lowercase.
    metric_id = models.ForeignKey(Metric, models.DO_NOTHING, db_column='Metric_id')  # Field name made lowercase.
    country_id = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_id')  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    tableto = models.CharField(db_column='TableTo', max_length=50)  # Field name made lowercase.
    insertminutes = models.IntegerField(db_column='InsertMinutes', blank=True, null=True)  # Field name made lowercase.
    daybefore = models.BooleanField(db_column='DayBefore')  # Field name made lowercase.
    dayafter = models.BooleanField(db_column='DayAfter', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Spot_Det_New'

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('fetchparams:wattsightdetlist')        


class SeecaoDet(models.Model):
    id = models.AutoField(primary_key=True)
    metric_id = models.ForeignKey(Metric, models.DO_NOTHING, db_column='Metric_id')  # Field name made lowercase.
    country_id = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_id')  # Field name made lowercase.
    entsoe_curves = models.CharField(max_length=100)
    fieldname = models.CharField(db_column='FieldName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seecao_Det'
        
    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('fetchparams:seecaodetlist')        

