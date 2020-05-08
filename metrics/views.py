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

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ValidationError

#from django_addanother.views import UpdatePopupMixin
#from django_addanother.views import CreatePopupMixin

from django.http import HttpResponse

from .models import Metric

class MetricForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Metric
        fields = ['name','abbr','comments','metric_category','active','fieldto_0']

import django_filters


class MetricFilter(django_filters.FilterSet):
    class Meta:
        model = Metric
        exclude = ('id',)
        fields = {
            'name': ['exact', ],
            'abbr': ['exact', ],
            'metric_category': ['exact', ],
            'fieldto_0': ['exact', ],
        }

from django_tables2.utils import A

class MetricTable(tables.Table):
    detail = tables.LinkColumn('metric:edit', args=[A('pk')], orderable=False, empty_values=[''])    
    class Meta:
        model = Metric
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name','...']

    def render_detail(self, record):
        #rev = reverse('Home', kwargs={'pk': str(record.pk)})
        #rev = reverse('country:list', kwargs={'pk': str(record.pk)})
        rev = reverse('metric:edit', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')


def MetricsDetailFiltered(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    data = Metric.objects.all()
    filter = MetricFilter(request.GET, queryset=data)
    table = MetricTable(filter.qs)

    RequestConfig(request, paginate={'per_page': 15}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                   'filter': filter,
                   'page_title': u'Metrics',
                   'form_name': u'Metrics',
                    'param_action1': reverse('metric:add'),
                    'param_action1_name': 'Προσθήκη'})



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
                   'form_name': u'Metric'})#,
#                    'param_action1': reverse('country:table'),
#                    'param_action1_name': 'Προσθήκη'})


#class CountryCreate(CreatePopupMixin,LoginRequiredMixin, UserPassesTestMixin, CreateView):
class MetricsCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Metric
    form_class = MetricForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class MetricsEdit(UpdateView):
    model = Metric
    form_class = MetricForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class MetricView(DetailView):
    model = Metric
    form_class = MetricForm
    template_name = 'General/metrics_detail.html'
    template_name = 'metrics_detail.html'

