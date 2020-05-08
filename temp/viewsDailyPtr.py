# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms

import django_tables2 as tables
from django_tables2 import RequestConfig
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
from .models import DailyPtr

ModelClassName = DailyPtr
ModelStr = 'dailyptr'
AppStr   = 'datapool'
PathStart = AppStr+':'+ModelStr
PageTitle = 'DailyPtr'
FormName  = 'DailyPtr'
DefComName = 'Προβολή'
ModelClassNameStr = 'DailyPTR'
Model_Fields = ['datetimeval','country','price','atc_volume']
Table_Sequence = ['datetimeval','country','detail','...']
Table_Exclude = []
Rows_Per_Page = 25
#######################

class CurrentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = ModelClassName
        fields = Model_Fields


class CurrentFilter(django_filters.FilterSet):
    datetimeval = django_filters.DateTimeFromToRangeFilter(widget=SplitDateTimeWidget())
    datetimeval = django_filters.DateTimeFromToRangeFilter(widget=SplitDateTimeWidget(attrs={'type': 'date'}))
    datetimeval.label = 'Διάστημα'
    
    class Meta:
        model = ModelClassName
        exclude = ('id',)
        fields = {
            'datetimeval' : [],
            'country' : ['exact', ], }

class CurrentTable(tables.Table):
    detail = tables.LinkColumn(PathStart+'view', args=[A('pk')], orderable=False, empty_values=[''])
    class Meta:
        model = ModelClassName
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = Table_Exclude
        sequence = Table_Sequence #['datetimeval','country','...']

    def render_detail(self, record):
        rev = reverse(PathStart+'view', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + f'><span style="color:red">{DefComName}</span></a>')


@login_required
@permission_required(f'{ModelClassName}.list_choice',raise_exception=True)
def DetailFiltered(request):
##    if not request.user.is_authenticated:
##        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    data = ModelClassName.objects.all()
    filter = CurrentFilter(request.GET, queryset=data)
    table = CurrentTable(filter.qs)

    RequestConfig(request, paginate={'per_page': Rows_Per_Page}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                   'filter': filter,
                   'page_title': PageTitle,
                   'form_name' : FormName})

#class Create(LoginRequiredMixin, UserPassesTestMixin, CreateView):
class Create(PermissionRequiredMixin, CreateView):
    permission_required = f'{ModelClassName}.add_choice'
    permission_denied_message = f'{ModelClassNameStr}'

    model = ModelClassName
    form_class = CurrentForm
    template_name = 'General/General_cu_form.html'

##    def test_func(self):
##        return True

class Edit(PermissionRequiredMixin, UpdateView):
    permission_required = f'{ModelClassName}.edit_choice'
    permission_denied_message = f'{ModelClassNameStr}'
    
    model = ModelClassName
    form_class = CurrentForm
    template_name = 'General/General_cu_form.html'

##    def test_func(self):
##        return True


class View(PermissionRequiredMixin , DetailView):
    permission_required = f'{ModelClassName}.view_choice'
    permission_denied_message = f'{ModelClassNameStr}'

    model = ModelClassName
    form_class = CurrentForm
    template_name = ModelStr+'_detail.html'

