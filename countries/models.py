# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=_('Ονόμα'),db_column='Name', max_length=50)  # Field name made lowercase.
    abbr = models.CharField(verbose_name=u'ISO3166-2',db_column='Abbr', max_length=10)  # Field name made lowercase.
    abbr_nrg = models.CharField(verbose_name=_('Συντ.NRG'),db_column='Abbr-nrg', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regionof = models.ForeignKey('self', models.DO_NOTHING, verbose_name=_('Επαρχεία της'),related_name='country_regionof', db_column='regionof', blank=True, null=True)  # Field name made lowercase.
    abbr_wattsight = models.CharField(verbose_name=_('Συντ.NRG'),db_column='Abbr_WattSight', max_length=10, blank=True, null=True)  # Field name made lowercase.
    abbr_entsoe = models.CharField(verbose_name=_('Συντ.ENTSOE'),db_column='Abbr_Entsoe', max_length=2, blank=True, null=True)  # Field name made lowercase.
    countryft = models.BooleanField(verbose_name=_('Διακίνηση'),db_column='CountryFT')  # Field name made lowercase.
    country_from = models.ForeignKey('self', models.DO_NOTHING, verbose_name=_('Χώρα Από'), related_name='country_from_country', db_column='Country_From_Id', blank=True, null=True)  # Field name made lowercase.
    country_to = models.ForeignKey('self', models.DO_NOTHING, verbose_name=_('Χώρα Προς'), related_name='country_to_country', db_column='Country_To_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'
        ordering = ('countryft','name')
        
#        error_name = 'Χώρες'
        #unique_together = (('country_from', 'country_to'),)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country:countrylist')



