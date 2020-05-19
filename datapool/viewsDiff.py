# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
import pandas as pd
from django_pandas.io import read_frame

from .models import *
from .forms import NameForm

import django_azure_nrg.settings as ds

Metric2Table={}
Metric2Table[1]=(SpotPrices,'SP')
Metric2Table[3]=(DailyPtr,'IP')
Metric2Table[4]=(FundamentalsWAv,'FWA')
Metric2Table[5]=(FundamentalsWFv,'FWF')
Metric2Table[6]=(FundamentalsWHv,'FWH')
Metric2Table[7]=(FundamentalsMOv,'FMO')
Metric2Table[8]=(FundamentalsMFv,'FMF')
Metric2Table[9]=(FundamentalsMSv,'FMS')
Metric2Table[11]=(SpotPrices,'SP1')


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        print('Leonidas0')
        if form.is_valid():
            panda = pd.DataFrame()
            DateFrom = form.cleaned_data['dtf_select']
            DateTo   = form.cleaned_data['dtt_select']
            Country1  = form.cleaned_data['cnt1_select']
            Country2  = form.cleaned_data['cnt2_select']
            Country3  = form.cleaned_data['cnt3_select']
            Metric1   = form.cleaned_data['met1_select']
            Metric2   = form.cleaned_data['met2_select']
            print('1++++++++',Metric1,Metric1.id)
            print('2++++++++',Metric2,Metric2.id)

            if Metric1.id in Metric2Table.keys():
                tmpmt = Metric2Table[Metric1.id]
                panda=addmetric(panda,Country1,DateFrom,DateTo,tmpmt[0],tmpmt[1])
            if Metric2.id in Metric2Table.keys():
                tmpmt = Metric2Table[Metric2.id]
                panda=addmetric(panda,Country1,DateFrom,DateTo,tmpmt[0],tmpmt[1])

                 
            if Country2 is None:
                pass
            else:
                if Metric1.id in Metric2Table.keys():
                    tmpmt = Metric2Table[Metric1.id]
                    panda=addmetric(panda,Country2,DateFrom,DateTo,tmpmt[0],tmpmt[1])
                if Metric2.id in Metric2Table.keys():
                    tmpmt = Metric2Table[Metric2.id]
                    panda=addmetric(panda,Country2,DateFrom,DateTo,tmpmt[0],tmpmt[1])

            if Country3 is None:
                pass
            else:
                if Metric1.id in Metric2Table.keys():
                    tmpmt = Metric2Table[Metric1.id]
                    panda=addmetric(panda,Country3,DateFrom,DateTo,tmpmt[0],tmpmt[1])
                if Metric2.id in Metric2Table.keys():
                    tmpmt = Metric2Table[Metric2.id]
                    panda=addmetric(panda,Country3,DateFrom,DateTo,tmpmt[0],tmpmt[1])

            ds.GlobDict[1] = panda.columns
            ds.PandasDict[1] = panda
            
            ##print('datafields',datafields)
            #return DetailFiltered(request,panda,datafields)
            #return HttpResponse(panda.to_html())
            return HttpResponseRedirect(reverse('datapool:viewdiff0',args=(1,)))
            #return DetailFiltered(request,1)

    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})



import django_tables2 as tables
from django_tables2 import RequestConfig
from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport


class CurrentTable(ExportMixin, tables.Table):
    datetimeval = tables.Column()
    Day         = tables.Column()
    Hour        = tables.Column()

    Field0 = tables.Column()
    Field1 = tables.Column()
    Field2 = tables.Column()
    Field3 = tables.Column()
    Field4 = tables.Column()
    Field5 = tables.Column()
    Field6 = tables.Column()
    Field7 = tables.Column()
    Field8 = tables.Column()
    Field9 = tables.Column()
    Field10 = tables.Column()    
    Field11 = tables.Column()
    Field12 = tables.Column()
    Field13 = tables.Column()
    Field14 = tables.Column()
    Field15 = tables.Column()
    Field16 = tables.Column()
    Field17 = tables.Column()
    Field18 = tables.Column()
    Field19 = tables.Column()
    Field20 = tables.Column()    
    Field21 = tables.Column()
    Field22 = tables.Column()
    Field23 = tables.Column()
    Field24 = tables.Column()
    Field25 = tables.Column()
    Field26 = tables.Column()
    Field27 = tables.Column()
    Field28 = tables.Column()
    Field29 = tables.Column()
    Field30 = tables.Column()    
    Field31 = tables.Column()
    Field32 = tables.Column()
    Field33 = tables.Column()
    Field34 = tables.Column()
    Field35 = tables.Column()
    Field36 = tables.Column()
    Field37 = tables.Column()
    Field38 = tables.Column()
    Field39 = tables.Column()
    Field40 = tables.Column()    

    prefixed_order_by_field='datetimeval'
        
    class Meta:
        attrs = {'class': 'paleblue'}
        sequence = ['datetimeval','...']

def DetailFiltered(request,pk):

    data=ds.PandasDict[1]
    glob=ds.GlobDict[1]
    
    data1=data.fillna(0)
    dlist=[]
    rt=0
    for index,row in data1.iterrows():
        d={}
        d['datetimeval'] = index
        d['Day'] = index.day
        d['Hour'] = index.hour
        rl=len(row)
        for z in range(rl):
            d['Field'+str(z)]=row[z]
        dlist.append(d)

    data=dlist
    table = CurrentTable(dlist)
    for x in range(rl):
        table.columns['Field'+str(x)].column.verbose_name=glob[x]

    for x in range(rl,41):
        table.columns['Field'+str(x)].column.visible=False
            
    


    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table ,exclude_columns = ("detail", ))
        return exporter.response("table.{}".format(export_format))
    

    PageTitle = 'Check Diff'
    FormName = 'Check Diff'
    RequestConfig(request, paginate={'per_page': 50}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
##                   'filter': filter,
                   'page_title': PageTitle,
                   'form_name' : FormName,})
        
        


def addmetric(panda,Country,DateFrom,DateTo,DataModel=FundamentalsWFv,DataModel_abbr='WFV'):
    df = str(DateFrom)
    dt = str(DateTo)
    qs=DataModel.objects.filter(country_id=Country).filter(datetimeval__gte=df).filter(datetimeval__lte=dt)
    df = read_frame(qs)#,index='datetimeval')
    #df=qs.to_dataframe(index='datetimeval')
    t=df.columns[3:]
    print(t)
    for n in t:
        tmp=df.rename(columns={n:n+'_'+DataModel_abbr+'_'+Country.abbr.strip()})
        df=tmp
    tmp=df.drop(columns='id')
    df=tmp.drop(columns='country')
    df.reset_index(drop=True)
    df1=df.set_index('datetimeval')
    #tmp=df1.drop(columns='id')
    if len(df1)>0:
        dd = pd.concat([panda,df1],axis=1)
    else:
        dd=panda
    return dd
