from django.db import models
from django.urls import reverse

class MetricCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    abbr = models.CharField(db_column='Abbr', max_length=10)  # Field name made lowercase.
    typeofdata = models.IntegerField(db_column='TypeOfData', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Metric_Category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('metric:categorylist')        




class TableParam(models.Model):
    id = models.AutoField(primary_key=True)
    table_name = models.CharField(db_column='Table_Name', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table_Param'

    def __str__(self):
        return self.table_name

    def get_absolute_url(self):
        return reverse('metric:tableslist')        




class FieldParam(models.Model):
    id = models.AutoField(primary_key=True)
    table = models.ForeignKey('TableParam', models.DO_NOTHING, db_column='Table_Id')  # Field name made lowercase.
    field_name = models.CharField(db_column='Field_Name', max_length=50)  # Field name made lowercase.
    field_description = models.CharField(db_column='Field_Description', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Field_Param'

    def __str__(self):
        return self.field_name + ' - '  + self.table.table_name

    def get_absolute_url(self):
        return reverse('metric:fieldslist')        


class Metric(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    abbr = models.CharField(db_column='Abbr', max_length=15)  # Field name made lowercase.
    uofm_id = models.IntegerField(db_column='UofM_Id', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    metric_category = models.ForeignKey('MetricCategory', models.DO_NOTHING, db_column='Metric_Category_Id')  # Field name made lowercase.
    name1 = models.CharField(db_column='Name1', max_length=150)  # Field name made lowercase.
    typeofmetric = models.IntegerField(db_column='TypeOfMetric', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    tableto = models.CharField(db_column='TableTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fieldto = models.CharField(db_column='FieldTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fieldto_0 = models.ForeignKey(FieldParam, models.DO_NOTHING, db_column='FieldTo_Id', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'Metric'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('metric:list')        

