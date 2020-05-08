# Generated by Django 3.0 on 2020-04-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdatedMC',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('datetimeval', models.DateField(db_column='DateTimeVal')),
                ('status_ok', models.BooleanField(db_column='Status_OK')),
                ('status_datetimeval', models.DateTimeField(db_column='Status_DateTimeVal')),
                ('commects', models.CharField(blank=True, db_column='Commects', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Updated_MC',
                'ordering': ['-datetimeval', 'metric_id', 'country_id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='View1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetimeval', models.DateTimeField(db_column='DateTimeVal')),
                ('atc_volume', models.DecimalField(blank=True, db_column='ATC_Volume', decimal_places=4, max_digits=10, null=True)),
                ('price_forecast', models.DecimalField(blank=True, db_column='Price_Forecast', decimal_places=4, max_digits=10, null=True)),
                ('price_actual', models.DecimalField(blank=True, db_column='Price_Actual', decimal_places=4, max_digits=10, null=True)),
                ('wav_consumption', models.DecimalField(blank=True, db_column='WAV_Consumption', decimal_places=4, max_digits=10, null=True)),
                ('wav_wind', models.DecimalField(blank=True, db_column='WAV_Wind', decimal_places=4, max_digits=10, null=True)),
                ('wav_pv', models.DecimalField(blank=True, db_column='WAV_PV', decimal_places=4, max_digits=10, null=True)),
                ('wav_nuclear', models.DecimalField(blank=True, db_column='WAV_Nuclear', decimal_places=4, max_digits=10, null=True)),
                ('wav_coal', models.DecimalField(blank=True, db_column='WAV_Coal', decimal_places=4, max_digits=10, null=True)),
                ('wav_lignite', models.DecimalField(blank=True, db_column='WAV_Lignite', decimal_places=4, max_digits=10, null=True)),
                ('wav_ccgt', models.DecimalField(blank=True, db_column='WAV_CCGT', decimal_places=4, max_digits=10, null=True)),
                ('wav_hydro', models.DecimalField(blank=True, db_column='WAV_Hydro', decimal_places=4, max_digits=10, null=True)),
                ('wfv_wind', models.DecimalField(blank=True, db_column='WFV_Wind', decimal_places=4, max_digits=10, null=True)),
                ('wfv_pv', models.DecimalField(blank=True, db_column='WFV_PV', decimal_places=4, max_digits=10, null=True)),
                ('wfv_nuclear', models.DecimalField(blank=True, db_column='WFV_Nuclear', decimal_places=4, max_digits=10, null=True)),
                ('wfv_coal', models.DecimalField(blank=True, db_column='WFV_Coal', decimal_places=4, max_digits=10, null=True)),
                ('wfv_lignite', models.DecimalField(blank=True, db_column='WFV__Lignite', decimal_places=4, max_digits=10, null=True)),
                ('wfv_ccgt', models.DecimalField(blank=True, db_column='WFV_CCGT', decimal_places=4, max_digits=10, null=True)),
                ('mov_consumption', models.DecimalField(blank=True, db_column='MOV_Consumption', decimal_places=4, max_digits=10, null=True)),
                ('mov_pv', models.DecimalField(blank=True, db_column='MOV_PV', decimal_places=4, max_digits=10, null=True)),
                ('mov_wind', models.DecimalField(blank=True, db_column='MOV_Wind', decimal_places=4, max_digits=10, null=True)),
                ('msv_consumption', models.DecimalField(blank=True, db_column='MSV_Consumption', decimal_places=4, max_digits=10, null=True)),
                ('msv_wind', models.DecimalField(blank=True, db_column='MSV_Wind', decimal_places=4, max_digits=10, null=True)),
                ('msv_pv', models.DecimalField(blank=True, db_column='MSV_PV', decimal_places=4, max_digits=10, null=True)),
                ('wfv_hydro', models.DecimalField(blank=True, db_column='WFV_Hydro', decimal_places=4, max_digits=10, null=True)),
                ('whv_consumption', models.DecimalField(blank=True, db_column='WHV_Consumption', decimal_places=4, max_digits=10, null=True)),
                ('whv_wind', models.DecimalField(blank=True, db_column='WHV_Wind', decimal_places=4, max_digits=10, null=True)),
                ('whv_pv', models.DecimalField(blank=True, db_column='WHV_PV', decimal_places=4, max_digits=10, null=True)),
                ('whv_hydro', models.DecimalField(blank=True, db_column='WHV_Hydro', decimal_places=4, max_digits=10, null=True)),
                ('mfv_consumption', models.DecimalField(blank=True, db_column='MFV_Consumption', decimal_places=4, max_digits=10, null=True)),
                ('mfv_wind', models.DecimalField(blank=True, db_column='MFV_Wind', decimal_places=4, max_digits=10, null=True)),
                ('mfv_pv', models.DecimalField(blank=True, db_column='MFV_PV', decimal_places=4, max_digits=10, null=True)),
                ('wfv_consumption', models.DecimalField(blank=True, db_column='WFV_Consumption', decimal_places=4, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'View_1',
                'managed': False,
            },
        ),
    ]
