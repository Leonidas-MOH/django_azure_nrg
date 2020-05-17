from django.db import models
from django.urls import reverse


class ScheduledTask(models.Model):
    id = models.AutoField(primary_key=True)    
    scheduler = models.ForeignKey('Scheduler', models.DO_NOTHING, db_column='Scheduler_Id')  # Field name made lowercase.
    timefrom = models.TimeField(db_column='TimeFrom')  # Field name made lowercase.
    timeto = models.TimeField(db_column='TimeTo')  # Field name made lowercase.
    task = models.ForeignKey('Task', models.DO_NOTHING, db_column='Task_id')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scheduled_Task'

    def __str__(self):
        return self.description.strip()

    def get_absolute_url(self):
        return reverse('scheduler:scheduledtasklist')        


class Scheduler(models.Model):
    id = models.AutoField(primary_key=True)    
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scheduler'

    def __str__(self):
        return self.name.strip()

    def get_absolute_url(self):
        return reverse('scheduler:schedulerlist')        


class Task(models.Model):
    id = models.AutoField(primary_key=True)    
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=250)  # Field name made lowercase.
    code = models.CharField(max_length=250)
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task'

    def __str__(self):
        return self.name.strip()

    def get_absolute_url(self):
        return reverse('scheduler:tasklist')        


class TaskParam(models.Model):
    id = models.AutoField(primary_key=True)    
    task = models.ForeignKey(Task, models.DO_NOTHING, db_column='Task_Id')  # Field name made lowercase.
    param_name = models.CharField(db_column='Param_Name', max_length=100)  # Field name made lowercase.
    param_value = models.CharField(db_column='Param_Value', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task_Param'

    def __str__(self):
        return self.param_name.strip()

    def get_absolute_url(self):
        return reverse('scheduler:taskparamlist')        
        

class ScheduleLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.
    task = models.ForeignKey(Task, models.DO_NOTHING, db_column='Task_Id')  # Field name made lowercase.
    scheduled_task = models.ForeignKey(ScheduledTask, models.DO_NOTHING, db_column='Scheduled_Task_Id')  # Field name made lowercase.
    log = models.TextField(db_column='Log')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedule_Log'
        ordering  = ['-datetime']

    def __str__(self):
        return self.task.strip()  + ' ' + self.scheduled_task +str(self.datetime)

    def get_absolute_url(self):
        return reverse('scheduler:scheduleloglist')        

        
