from django.db import models
from django.urls import reverse
from countries.models import *
from metrics.models import *


class DailyPtr(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    atc_volume = models.DecimalField(db_column='ATC_Volume', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Daily_PTR'
        unique_together = (('datetimeval', 'country'),)
        ordering = ['-datetimeval', 'country']

    def __str__(self):
        #return str(self.datetimeval) + ' ' + self.country
        return str(self.datetimeval)

    def get_absolute_url(self):
        return reverse('datapool:dailyptrlist')        

        

class FundamentalsMFv(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    consumption = models.DecimalField(db_column='Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wind = models.DecimalField(db_column='Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pv = models.DecimalField(db_column='PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fundamentals_M_FV'
        unique_together = (('datetimeval', 'country'),)
        ordering = ['-datetimeval', 'country']

    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country

    def get_absolute_url(self):
        return reverse('datapool:fundamentalsMFvlist')        

class FundamentalsMOv(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    consumption = models.DecimalField(db_column='Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wind = models.DecimalField(db_column='Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pv = models.DecimalField(db_column='PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fundamentals_M_OV'
        unique_together = (('datetimeval', 'country'),)
        ordering = ['-datetimeval', 'country']

    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country

    def get_absolute_url(self):
        return reverse('datapool:fundamentalsMOvlist')        


class FundamentalsMSv(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    consumption = models.DecimalField(db_column='Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wind = models.DecimalField(db_column='Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pv = models.DecimalField(db_column='PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fundamentals_M_SV'
        unique_together = (('datetimeval', 'country'),)
        ordering = ['-datetimeval', 'country']

    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country

    def get_absolute_url(self):
        return reverse('datapool:fundamentalsMSvlist')        

class FundamentalsWAv(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    consumption = models.DecimalField(db_column='Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wind = models.DecimalField(db_column='Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pv = models.DecimalField(db_column='PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nuclear = models.DecimalField(db_column='Nuclear', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    coal = models.DecimalField(db_column='Coal', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lignite = models.DecimalField(db_column='Lignite', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ccgt = models.DecimalField(db_column='CCGT', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hydro = models.DecimalField(db_column='Hydro', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    commercial_flow = models.DecimalField(db_column='Commercial_flow', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ntc = models.DecimalField(db_column='NTC', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fundamentals_W_AV'
        unique_together = (('datetimeval', 'country'),)
        ordering = ['-datetimeval', 'country']

    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country

    def get_absolute_url(self):
        return reverse('datapool:fundamentalsWAvlist')        
        

class FundamentalsWFv(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    consumption = models.DecimalField(db_column='Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wind = models.DecimalField(db_column='Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pv = models.DecimalField(db_column='PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nuclear = models.DecimalField(db_column='Nuclear', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    net_imports = models.DecimalField(db_column='Net_Imports', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    coal = models.DecimalField(db_column='Coal', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lignite = models.DecimalField(db_column='Lignite', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ccgt = models.DecimalField(db_column='CCGT', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hydro = models.DecimalField(db_column='Hydro', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fundamentals_W_FV'
        unique_together = (('datetimeval', 'country'),)
        ordering = ['-datetimeval', 'country']

    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country.name

    def get_absolute_url(self):
        return reverse('datapool:fundamentalsWFvlist')        

class FundamentalsWHv(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    consumption = models.DecimalField(db_column='Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wind = models.DecimalField(db_column='Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pv = models.DecimalField(db_column='PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hydro = models.DecimalField(db_column='Hydro', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fundamentals_W_HV'
        unique_together = (('datetimeval', 'country'),)
        ordering = ['-datetimeval', 'country']

    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country

    def get_absolute_url(self):
        return reverse('datapool:fundamentalsWHvlist')        
        

class SpotPrices(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    price_forecast = models.DecimalField(db_column='Price_Forecast', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    price_actual = models.DecimalField(db_column='Price_Actual', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Spot_Prices'
        unique_together = (('datetimeval', 'country'),)
        ordering = ['-datetimeval', 'country']

    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country

    def get_absolute_url(self):
        return reverse('datapool:spotpriceslist')        
        

class UpdatedMC(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateField(db_column='DateTimeVal')  # Field name made lowercase.
    metric_id = models.ForeignKey(Metric, models.DO_NOTHING, db_column='Metric_id')  # Field name made lowercase.
    country_id = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    status_ok = models.BooleanField(db_column='Status_OK')  # Field name made lowercase.
    status_datetimeval = models.DateTimeField(db_column='Status_DateTimeVal')  # Field name made lowercase.
    commects = models.CharField(db_column='Commects', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Updated_MC'
        unique_together = (('datetimeval', 'metric_id', 'country_id'),)
        ordering = ['-datetimeval', 'metric_id', 'country_id']

    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country_id + ' ' + self.metric_id

    def get_absolute_url(self):
        return reverse('datapool:updatedmclist')


class View1(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetimeval = models.DateTimeField(db_column='DateTimeVal')  # Field name made lowercase.
    country_id = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_Id')  # Field name made lowercase.
    #price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    atc_volume = models.DecimalField(db_column='ATC_Volume', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    price_forecast = models.DecimalField(db_column='Price_Forecast', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    price_actual = models.DecimalField(db_column='Price_Actual', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wav_consumption = models.DecimalField(db_column='WAV_Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wav_wind = models.DecimalField(db_column='WAV_Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wav_pv = models.DecimalField(db_column='WAV_PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wav_nuclear = models.DecimalField(db_column='WAV_Nuclear', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wav_coal = models.DecimalField(db_column='WAV_Coal', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wav_lignite = models.DecimalField(db_column='WAV_Lignite', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wav_ccgt = models.DecimalField(db_column='WAV_CCGT', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wav_hydro = models.DecimalField(db_column='WAV_Hydro', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wfv_wind = models.DecimalField(db_column='WFV_Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wfv_pv = models.DecimalField(db_column='WFV_PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wfv_nuclear = models.DecimalField(db_column='WFV_Nuclear', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wfv_coal = models.DecimalField(db_column='WFV_Coal', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wfv_lignite = models.DecimalField(db_column='WFV_Lignite', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    wfv_ccgt = models.DecimalField(db_column='WFV_CCGT', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mov_consumption = models.DecimalField(db_column='MOV_Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mov_pv = models.DecimalField(db_column='MOV_PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mov_wind = models.DecimalField(db_column='MOV_Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    msv_consumption = models.DecimalField(db_column='MSV_Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    msv_wind = models.DecimalField(db_column='MSV_Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    msv_pv = models.DecimalField(db_column='MSV_PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wfv_hydro = models.DecimalField(db_column='WFV_Hydro', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    whv_consumption = models.DecimalField(db_column='WHV_Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    whv_wind = models.DecimalField(db_column='WHV_Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    whv_pv = models.DecimalField(db_column='WHV_PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    whv_hydro = models.DecimalField(db_column='WHV_Hydro', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mfv_consumption = models.DecimalField(db_column='MFV_Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mfv_wind = models.DecimalField(db_column='MFV_Wind', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mfv_pv = models.DecimalField(db_column='MFV_PV', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wfv_consumption = models.DecimalField(db_column='WFV_Consumption', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'View_1'


    def __str__(self):
        return str(self.datetimeval) + ' ' + self.country_id

    def get_absolute_url(self):
        return reverse('datapool:view1list')
    
