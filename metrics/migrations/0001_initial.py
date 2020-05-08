# Generated by Django 2.1.15 on 2020-04-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldParam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('field_name', models.CharField(db_column='Field_Name', max_length=50)),
                ('field_description', models.CharField(blank=True, db_column='Field_Description', max_length=250, null=True)),
            ],
            options={
                'db_table': 'Field_Param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=150)),
                ('abbr', models.CharField(db_column='Abbr', max_length=15)),
                ('uofm_id', models.IntegerField(blank=True, db_column='UofM_Id', null=True)),
                ('comments', models.CharField(blank=True, db_column='Comments', max_length=255, null=True)),
                ('name1', models.CharField(db_column='Name1', max_length=150)),
                ('typeofmetric', models.IntegerField(blank=True, db_column='TypeOfMetric', null=True)),
                ('active', models.BooleanField(blank=True, db_column='Active', null=True)),
                ('tableto', models.CharField(blank=True, db_column='TableTo', max_length=50, null=True)),
                ('fieldto', models.CharField(blank=True, db_column='FieldTo', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Metric',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetricCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('abbr', models.CharField(db_column='Abbr', max_length=10)),
                ('typeofdata', models.IntegerField(blank=True, db_column='TypeOfData', null=True)),
                ('active', models.BooleanField(blank=True, db_column='Active', null=True)),
            ],
            options={
                'db_table': 'Metric_Category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TableParam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('table_name', models.CharField(db_column='Table_Name', max_length=50)),
                ('description', models.CharField(db_column='Description', max_length=250)),
            ],
            options={
                'db_table': 'Table_Param',
                'managed': False,
            },
        ),
    ]
