# -*- coding: cp1253 -*-
from django import forms
from django.contrib.admin import widgets
from metrics.models import MetricCategory
from countries.models import Country

import datetime 

class NameForm(forms.Form):
    cnt1_select = forms.ModelChoiceField(queryset=None,required=True, label='Χώρα 1*    ')
    cnt2_select = forms.ModelChoiceField(queryset=None,required=False,label='Χώρα 2     ')
    cnt3_select = forms.ModelChoiceField(queryset=None,required=False,label='Χώρα 3     ')
    met1_select = forms.ModelChoiceField(queryset=None,required=True, label='Metric 1*  ')
    met2_select = forms.ModelChoiceField(queryset=None,required=False, label='Metric 2   ')
    dtf_select  = forms.DateField(initial=datetime.datetime.now()-datetime.timedelta(30),required=True,label='Από     ')
    dtt_select  = forms.DateField(initial=datetime.date.today,required=True,label='Έως       ')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cnt1_select'].queryset = Country.objects.filter(countryft=0)
        self.fields['cnt2_select'].queryset = Country.objects.filter(countryft=0)
        self.fields['cnt3_select'].queryset = Country.objects.filter(countryft=0)        
        self.fields['met1_select'].queryset = MetricCategory.objects.all()
        self.fields['met2_select'].queryset = MetricCategory.objects.all()
