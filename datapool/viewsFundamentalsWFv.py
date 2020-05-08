# -*- coding: utf-8 -*-
from django.shortcuts import render

# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms

import django_tables2 as tables
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.html import mark_safe
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

#from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.forms import SplitDateTimeWidget

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ValidationError

#from django_addanother.views import UpdatePopupMixin
#from django_addanother.views import CreatePopupMixin

from django.http import HttpResponse

from .models import FundamentalsWFv

#######################
ModelClassName = FundamentalsWFv
ModelStr = 'fundamentalsWFv'
AppStr   = 'datapool'
PathStart = AppStr+':'+ModelStr
PageTitle = 'fundamentalsWFv'
FormName  = 'fundamentalsWFv'
DefComName = 'Προβολή'
#######################

class CurrentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = ModelClassName
        fields = ['datetimeval','country','consumption','wind','pv','nuclear',
                  'coal','lignite','ccgt','hydro','net_imports']

import django_filters


class CurrentFilter(django_filters.FilterSet):
    datetimeval = django_filters.DateTimeFromToRangeFilter(widget=SplitDateTimeWidget())
    datetimeval = django_filters.DateTimeFromToRangeFilter(widget=SplitDateTimeWidget(attrs={'type': 'date'}))
    datetimeval.label = 'Διάστημα'

    
    class Meta:
        model = ModelClassName
        exclude = ('id',)
        fields = {
            'datetimeval' : [],
            'country' : ['exact', ],            
        }

from django_tables2.utils import A

class CurrentTable(tables.Table):
    #detail = tables.LinkColumn('fetchparams:meteoedit', args=[A('pk')], orderable=False, empty_values=[''])
    detail = tables.LinkColumn(PathStart+'view', args=[A('pk')], orderable=False, empty_values=[''])
    AppStr
    class Meta:
        model = ModelClassName
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = []
        sequence = ['datetimeval','country','...']

    def render_detail(self, record):
        #rev = reverse('Home', kwargs={'pk': str(record.pk)})
        #rev = reverse('country:list', kwargs={'pk': str(record.pk)})
        rev = reverse(PathStart+'view', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + f'><span style="color:red">{DefComName}</span></a>')


def DetailFiltered(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    data = ModelClassName.objects.all()
    filter = CurrentFilter(request.GET, queryset=data)
    table = CurrentTable(filter.qs)

    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                   'filter': filter,
                   'page_title': PageTitle,
                   'form_name' : FormName})#,
##                    'param_action1': reverse(PathStart+'view'),
##                    'param_action1_name': 'Προσθήκη'})



# @login_required
#def CountryList(request):
def Home0(request):    
    #    if not request.user.is_authenticated:
    #        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = MetricTable(Metric.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                   'page_title': u'Metric',
                   'form_name': u'Metric', #})#,
                    'param_action1': reverse(PathStart+'view'),
                    'param_action1_name': 'Προσθήκη'})
#                    'param_action1': reverse('country:table'),
#                    'param_action1_name': 'Προσθήκη'})


#class CountryCreate(CreatePopupMixin,LoginRequiredMixin, UserPassesTestMixin, CreateView):
class Create(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ModelClassName
    form_class = CurrentForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class Edit(UpdateView):
    model = ModelClassName
    form_class = CurrentForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class View(DetailView):
    model = ModelClassName
    form_class = CurrentForm
    template_name = 'General/metrics_detail.html'
    template_name = ModelStr+'_detail.html'
    #template_name = 'General/General_cu_form2.html'

