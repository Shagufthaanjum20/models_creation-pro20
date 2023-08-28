from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    tn=input('enter the topic name : ')
    to=topic.objects.get_or_create(topic_name=to)[0]
    to.save()
    return HttpResponse('Data is inserted')
def insert_webpage(request):
    tn=input('enter topic_name: ')
    n=input('enter name: ')

    u=input('enter url: ')
    TO=topic.objects.get(topic_name=TN)
    wo=webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0] 
    wo.save() 
    return HttpResponse ('Data inserted')
def insert_Ac(request):
    n=input('enter name : ' )
    wo=webpage.objects.get(name=n)
    d=input('enter date : ')
    a=input('enter author : ')
    ao=accessRecords.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    return HttpResponse('Data inserted')
    
      







def display_topic(request):
    QSTO=topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)


def display_webpages(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)


def display_access(request):
    QSAO=accessRecords.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_access.html',d)


def insert_topic(request):
    topic_name=input('enter topic_name')
    to=Topic.objects.get_or_create(topic_name=topic_name)[0]
    to.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)



def insert_webpage(request):
    tn=input('enter topic_name')
    na=input('enter name')
    ur=input('enter url')

    tn=Topic.objects.get(topic_name=tn)

    to=Webpage.objects.get_or_create(topic_name=to,name=na,url=ur)[0]
    to.save()

    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)