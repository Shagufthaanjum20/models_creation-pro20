from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    TN=input('enter the topic name : ')
    TO=topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    return HttpResponse('Data is inserted')
def insert_webpage(request):
    TN=input('enter topic_name: ')
    n=input('enter name: ')

    u=input('enter url: ')
    TO=topic.objects.get(topic_name=TN)
    WO=webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0] 
    WO.save() 
    return HttpResponse ('Data inserted')
def insert_Ac(request):
    n=input('enter name : ' )
    wo=webpage.objects.get(name=n)
    d=input('enter date : ')
    a=input('enter author : ')
    ao=AccessRecords.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    return HttpResponse('Data inserted')
    