# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms

import django_tables2 as tables
from django_tables2 import RequestConfig
from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport

from django.utils.html import mark_safe
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import AccessMixin 
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

import django_filters
from django.forms import SplitDateTimeWidget

from django.http import HttpResponse
from django_tables2.utils import A


#######################
from .models import MeteoDetNew

ModelClassName = MeteoDetNew

ModelStr = 'meteo'
AppStr   = 'fetchparams'

PathStart = AppStr+':'+ModelStr 

PageTitle = 'Meteologica'
FormName  = 'Meteologica'

DefComName = 'Προβολή'
DefComAction = 'view'

AltComName = 'Προθήκη'
AltComAction = 'add'

AddComName = 'Προθήκη'
AddComAction = 'add'
EditComName = 'Μεταβολή'
EditComAction = 'edit'
ViewComName = 'Προβολή'
ViewComAction = 'view'

ModelClassNameStr = 'Meteo'
Model_Fields = ['metric_id','country_id','active','daybefore','dayafter','ftppath','filename','insertminutes',
                'fieldname','timefrom','timeto','timeselection',
                'headerrow','usetimeframe']
Table_Sequence = ['metric_id','country_id','detail','detailed','...']
Table_Exclude = ['id','fieldname','ftppath','timefrom','timeto','timeselection','headerrow','usetimeframe','fieldto','tableto']
Rows_Per_Page = 25

#--------------------------

class CurrentFilter(django_filters.FilterSet):
##    datetimeval = django_filters.DateTimeFromToRangeFilter(widget=SplitDateTimeWidget())
##    datetimeval = django_filters.DateTimeFromToRangeFilter(widget=SplitDateTimeWidget(attrs={'type': 'date'}))
##    datetimeval.label = 'Διάστημα'
    
    class Meta:
        model = ModelClassName
        exclude = ('id',)
        fields = {
            'metric_id' : ['exact', ],
            'country_id' : ['exact', ],
            'filename' : ['icontains'],
            'active': ['exact', ],
        }


#######################

class CurrentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = ModelClassName
        fields = Model_Fields

class CurrentTable(ExportMixin, tables.Table):
    detail = tables.LinkColumn(PathStart+'view', args=[A('pk')], orderable=False, empty_values=[''])
    detailed = tables.LinkColumn(PathStart+'edit', args=[A('pk')], orderable=False, empty_values=[''])    
    class Meta:
        model = ModelClassName
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = Table_Exclude
        sequence = Table_Sequence #['datetimeval','country','...']
        

    def render_detail(self, record):
        rev = reverse(PathStart+'view', kwargs={'pk': str(record.id)})
        return mark_safe('<a href=' + rev + f'><span style="color:red">{DefComName}</span></a>')
    def render_detailed(self, record):
        rev = reverse(PathStart+'edit', kwargs={'pk': str(record.id)})
        return mark_safe('<a href=' + rev + f'><span style="color:green">{EditComName}</span></a>')


@login_required
@permission_required(f'{AppStr}.view_{ModelStr}',raise_exception=True)
def DetailFiltered(request):

    data = ModelClassName.objects.all()
    filter = CurrentFilter(request.GET, queryset=data)
    table = CurrentTable(filter.qs)

    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table ,exclude_columns = ('detail','detailed' ))
        return exporter.response("table.{}".format(export_format))
    

    RequestConfig(request, paginate={'per_page': Rows_Per_Page}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                   'filter': filter,
                   'page_title': PageTitle,
                   'form_name' : FormName,#})
                   'param_action1_name': AltComName,
                   'param_action1': reverse(PathStart+AltComAction),})


#class Create(LoginRequiredMixin, UserPassesTestMixin, CreateView):
class Create(PermissionRequiredMixin, CreateView):
    permission_required = f'{AppStr}.add_{ModelStr}'
    permission_denied_message = f'{ModelClassNameStr}'

    model = ModelClassName
    form_class = CurrentForm
    template_name = 'General/General_cu_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['form_name'] = FormName
        return context

##    def test_func(self):
##        return True

class Edit(PermissionRequiredMixin, UpdateView):
    permission_required = f'{AppStr}.edit_{ModelStr}'
    permission_denied_message = f'{ModelClassNameStr}'
    
    model = ModelClassName
    form_class = CurrentForm
    template_name = 'General/General_cu_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['form_name'] = FormName
        return context
    

class View(PermissionRequiredMixin , DetailView):
    permission_required = f'{AppStr}.view_{ModelStr}'
    permission_denied_message = f'{ModelClassNameStr}'

    model = ModelClassName
    form_class = CurrentForm
    template_name = ModelStr+'_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['form_name'] = FormName
        return context
