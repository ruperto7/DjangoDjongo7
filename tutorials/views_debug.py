#from django.shortcuts import render
from django.contrib.sessions.models import Session
#from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
#from rest_framework.decorators import api_view
import json
from django.http import HttpResponse

##
import pandas as pd 
from django.http import HttpResponse as hr
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
#@api_view(['GET'])
def sessionsAndUsers(request):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    #sessions.
    uid_list = []
    for session in sessions: 
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id' , None))
    return HttpResponse( showSettings())

def requestToJson(request):
       #json_data = json.loads(request.body.decode(encoding='UTF-8'))
       json_data = request.body.__doc__
       #print('Raw Data : %s' % json_data)
       #return HttpResponse('OK!')
       return json_data

def showSettings():
    astr, adict, alist ="","",""
    for s in dir(settings):
        s2 = getattr(settings, s)
        if (type(s2))==type('x'):
            astr+= s + ' : '+ getattr(settings, s)+'<br>'
        elif (type(s2))==type({'x':0}): 
            #adict+= s + ' : NOT S STRING it is a DICT <br>'
            try:
                adict+= s+': ' + json.dumps(s2)  +'<br>'
            except:
                adict+= s + ' : NOT S STRING it is a DICT <br>'   
        elif (type(s2))==type([{'x':0}]):    
            #alist+= s + ' : NOT S STRING it is a LIST <br>'    
            alist+= s +': '+ ''.join((str(e)+"***") for e in s2) + '<br>'   
    return  astr+'<br><br>'+ adict+'<br><br>'+alist
  
@csrf_exempt    #@api_view(['POST'])
def ApiHandler3(request):
    #if request.method != 'POST':
    #    return hr("POST request method is needed. <br /><br /> For more information, please contact totoarrieta@yahoo.com <br /><br />re: access to https://totoarrieta.pythonanywhere.com/api2/  <br /><br />Thank you!")
    ##ds = pd.read_csv( "https://covid.ourworldindata.org/data/owid-covid-data.csv", verbose=True)
    ds = pd.read_csv( "http://127.0.0.1:8000/static/owid-covid-data.csv", verbose=True)
    ds['TD_to_TC_R'] = ds.total_deaths/ds.total_cases
    rpt_date=ds[['date']].max()[0]  #'2020-04-13' # string of current report date YYYY-MM-DD
    #.to_string(index=False)
    ##ds=ds.iloc[:,[0,1,4,5,6]]#retain 2 columns i.e. location, total_cases total_deaths and TD_to_TC_R
    ds=ds.iloc[:,[2,3,4,7,21]]
    #ds2 = pd.read_csv( "./locations.csv", verbose=True )
    ##rpt_date=ds[['date']].max()[0]
    ds1B = ds[(ds.date.str.contains(rpt_date)) ] #& (ds.location != 'World' )
    ds2 = pd.read_csv( "http://127.0.0.1:8000/static/locations.csv", verbose=True )
    ds2 = ds2.iloc[:,[1,4]] #retain 2 columns i.e. location and population
    j=ds1B.set_index('location').join(ds2.set_index('location'))
    j['TCPR']=j.total_cases/j.population #NEW COLUMN
    j[j.population > 1e8].sort_values(['population' ], ascending=False)
    #j[j.population > 1e8].iloc[:,[0,4,9,10]].sort_values(['population' ], ascending=False)
    j[j.population > 1e8].sort_values(['population' ], ascending=False)
    topTCPR=j[j.population > 1e8].iloc[:,[0,1,2,3,5]].sort_values(['TCPR' ], ascending=False)
    topTCPR['location']=topTCPR.index
    topTCPR['idx']=topTCPR['TCPR']
    topTCPR2=topTCPR.set_index('idx')
    ##topTD_to_TC_R=j[j.population > 1e8].iloc[:,[1,0,5]].sort_values(['TCPR' ], ascending=False)
    #print(topTCPR2)
    return hr(topTCPR2.to_json()) # df.to_numpy()