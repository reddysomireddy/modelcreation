from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'topic.html',d)

def webpage(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.order_by('name')
    LWO=Webpage.objects.order_by('-name')
    LWO=Webpage.objects.order_by(Length('name'))
    LWO=Webpage.objects.order_by(Length('name').desc())
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(name__startswith='M')
    LWO=Webpage.objects.filter(name__endswith='i')
    LWO=Webpage.objects.filter(name__contains='raina')
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'webpage.html',d)

def access(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date='1982-04-23')
    LAO=AccessRecords.objects.filter(date__year='1982')
    LAO=AccessRecords.objects.filter(date__day='07')
    LAO=AccessRecords.objects.filter(date__year__gte='1980')
    
    
    d={'LAO':LAO}
    return render(request,'access.html',d)
    
