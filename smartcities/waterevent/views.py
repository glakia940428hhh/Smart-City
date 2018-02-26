from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db import connection

from .models import Location, Event, ObservReport, Region, Sensor,Pipe, WatershedPipe, Watershed
from django import forms
from django.forms import ModelForm
from django.template import loader



# Create your views here.
def index(request):

    return render(request, 'waterevent/index.html')

def map(request):
    return render(request, 'waterevent/map.html')

def EventList(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'waterevent/event_home.html', context)

    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'waterevent/index.html',context)




class EventCreate(ModelForm):
    class Meta:
        model = Event
        fields = ['eventId', 'description', 'type', 'date']
        labels = {
            'eventId': 'ID of the event',
            'description': 'description of the event',
            'type': 'type of the event',
        }


def Event_create(request, template_name='waterevent/event_form.html'):
    form = EventCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('waterevent:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def EventUpdate(request, pk, template_name='waterevent/event_form.html'):
    events = get_object_or_404(Event, pk=pk)
    form = EventCreate(request.POST or None, instance=events)
    if form.is_valid():
        form.save()

        return redirect('waterevent:eventlist')



    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def EventDelete(request, pk, template_name='waterevent/detail.html'):
    events = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        events.delete()
        return redirect('waterevent:eventlist')
    return render(request, template_name, {'object': events})


def EventListDelete(request, pk, template_name='waterevent/event_home.html'):
    events = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        events.delete()
        return redirect('waterevent:eventlist')
    return render(request, template_name, {'object': events})


def EventDelete(request,pk, template_name='waterevent/detail.html'):
    events = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        events.delete()
        return redirect('waterevent:index')
    return render(request, template_name,{'object':events})

def detail(request, pk):
    events = get_object_or_404(Event, pk=pk)
    context = {'events': events}
    return render(request, 'waterevent/detail.html', context)


'''
class EventUpdate(UpdateView):
    model = Event
    fields = ['eventId', 'description', 'type', 'date']

class EventDelete (DeleteView):
    model = Event
    success_url = reverse_lazy('index')

'''


def EventView(request, eventId):

    event = get_object_or_404(Event, pk=eventId)
    context = {'event': event}
    return render(request, 'waterevent/detail.html', context)


# ===========================Report=========================================

def report(request):
    report = ObservReport.objects.all()
    context = {'report': report}
    return render(request, 'waterevent/report_home.html', context)

class ReportCreate(ModelForm):
    class Meta:
        model = ObservReport
        fields = ['observId', 'date', 'observName', 'overflow']
        labels = {
            'observId': 'ID of the observer',
            'date': 'Date of adding this observation',
            'observName': 'Name of the observer',
            'overflow': 'Was there an overflow?',
        }


def Report_create(request, template_name='waterevent/report_form.html'):
    form = EventCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('waterevent:index')
    ctx = {}
    ctx["reportadd"] = form
    return render(request, template_name, ctx)


def ReportList(request):
    reports = ObservReport.objects.all()
    context = {'report': reports}
    return render(request, 'waterevent/report_home.html', context)

def Report_Update(request, pk, template_name='waterevent/report_form.html'):
    report = get_object_or_404(ObservReport, pk=pk)
    form = ReportCreate(request.POST or None, instance=report)
    if form.is_valid():
        form.save()
        return redirect('waterevent:reportlist')
    ctx = {"form": form}
    return render(request, template_name, ctx)


def Report_Delete(request, pk, template_name='waterevent/detail.html'):
    reports = get_object_or_404(ObservReport, pk=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('waterevent:reportlist')
    return render(request, template_name, {'object': reports})





def ReportListDelete(request, pk, template_name='waterevent/report_home.html'):
    reports = get_object_or_404(ObservReport, pk=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('waterevent:reportList')
    return render(request, template_name, {'object': reports})


def report_detail(request):
    if request.method == 'POST':
        reportid = (request.POST.get('tag'))
        reports = ObservReport.objects.raw('Select * from ObservReport where observId =  %s', [reportid])
        context = {'reports': reports}
        template = loader.get_template('waterevent/report_detail.html')
        return HttpResponse(template.render(context, request))

def ReportView(request, observId):
    reports = get_object_or_404(ObservReport, pk=observId)
    context = {'report': reports}
    return render(request, 'waterevent/report_detail.html', context)

    event = get_object_or_404(Event, pk = eventId)
    context = {'event':event}
    return render(request, 'waterevent/detail.html', context)

#sensor

def SensorList(request):
    sensors= Sensor.objects.all()
    context = {'sensors': sensors}
    return render(request, 'waterevent/sensor_home.html',context)


class SensorCreate(ModelForm):
    class Meta:
        model = Sensor
        fields = ['sensorId', 'volume', 'phLevel', 'contaminantLevel', 'date', 'observId']
        labels = {
            'sensorId': 'ID of the sensor',
            'volume': 'Volume of the sensor',
            'phLevel': 'phLevel of the sensor',
            'contaminantLevel': 'contaminantLevel of the sensor',
            'date': 'date of the sensor',
            'observId': 'ObserverID of the sensor'

        }


def Sensor_create(request, template_name='waterevent/sensor_form.html'):
            form = SensorCreate(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('waterevent:index')
            ctx = {}
            ctx["form"] = form
            return render(request, template_name, ctx)



def SensorUpdate(request,pk, template_name='waterevent/sensor_form.html'):
    sensors = get_object_or_404(Sensor, pk=pk)
    form = SensorCreate(request.POST or None, instance = sensors)
    if form.is_valid():
        form.save()
        return redirect('waterevent:sensorlist')
    ctx = {"form": form}
    return render(request, template_name, ctx)


def SensorDelete(request,pk, template_name='waterevent/sensor.html'):
    sensors = get_object_or_404(Sensor, pk=pk)
    if request.method == 'POST':
        sensors.delete()
        return redirect('waterevent:sensorlist')
    return render(request, template_name,{'object':sensors})


def sensor_detail(request):
    if request.method == 'POST':
        sensorid = (request.POST.get('tag'))
        sensors = ObservReport.objects.raw('Select * from Sensor where sensorId =  %s', [sensorid])
        context = {'sensors': sensors}
        template = loader.get_template('waterevent/sensor.html')
        return HttpResponse(template.render(context, request))

# ===========================Location=========================================

def location(request):
    location = Location.objects.all()
    context = {'location': location}
    return render(request, 'waterevent/location_home.html', context)

class LocationCreate(ModelForm):
    class Meta:
        model = Location
        fields = ['locationid', 'locname', 'loclatitude', 'loclongitude']
        labels = {
            'locationid': 'ID of the location',
            'locname': 'Location Name',
            'loclatitude': 'Location Latitude',
            'loclongitude': 'Location Longitude',
        }

def Location_create(request, template_name='waterevent/location_form.html'):
    form = LocationCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('waterevent:index')
    ctx = {}
    ctx["locationadd"] = form
    return render(request, template_name, ctx)

def LocationList(request):
    cursor = connection.cursor()
    cursor.execute("Select * from Location")
    locations = dictfetchall(cursor)
    context = {'location': locations}
    return render(request, 'waterevent/location_home.html', context)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def Location_Update(request, pk, template_name='waterevent/location_form.html'):
    location = get_object_or_404(Location, pk=pk)
    form = LocationCreate(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('waterevent:locationlist')
    ctx = {"form": form}
    return render(request, template_name, ctx)

def Location_Delete(request, pk, template_name='waterevent/detail.html'):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('waterevent:locationlist')
    return render(request, template_name, {'object': location})

def LocationListDelete(request, pk, template_name='waterevent/location_home.html'):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('waterevent:locationlist')
    return render(request, template_name, {'object': location})


def location_detail(request):
    if request.method == 'POST':
        locationId = str(request.POST.get('tag'))
        locations = Location.objects.raw('Select * from Location where locationId =  %s', [locationId])
        context = {'locations': locations}
        template = loader.get_template('waterevent/location_detail.html')
        return HttpResponse(template.render(context, request))

def LocationView(request, locationId):
    location = get_object_or_404(Location, pk=locationId)
    context = {'location': location}
    return render(request, 'waterevent/location_detail.html', context)

    location = get_object_or_404(Location, pk = locationId)
    context = {'location':location}
    return render(request, 'waterevent/detail.html', context)

# ===========================Region=========================================

def region(request):
    region = Region.objects.all()
    context = {'region': region}
    return render(request, 'waterevent/region_home.html', context)

class RegionCreate(ModelForm):
    class Meta:
        model = Region
        fields = ['regionid', 'regionname']
        labels = {
            'regionid': 'ID of the region',
            'regionname': 'Region Name',
        }


def Region_create(request, template_name='waterevent/region_form.html'):
    form = RegionCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('waterevent:index')
    ctx = {}
    ctx["regionadd"] = form
    return render(request, template_name, ctx)


def RegionList(request):
    cursor = connection.cursor()
    cursor.execute("Select * from Region")
    region = dictfetchall(cursor)
    context = {'region': region}
    return render(request, 'waterevent/region_home.html', context)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def Region_Update(request, pk, template_name='waterevent/region_form.html'):
    region = get_object_or_404(Region, pk=pk)
    form = RegionCreate(request.POST or None, instance=region)
    if form.is_valid():
        form.save()
        return redirect('waterevent:regionlist')
    ctx = {"form": form}
    return render(request, template_name, ctx)


def Region_Delete(request, pk, template_name='waterevent/region_home.html'):
    region = get_object_or_404(Region, pk=pk)
    if request.method == 'POST':
        region.delete()
        return redirect('waterevent:regionlist')
    return render(request, template_name, {'object': region})

def RegionListDelete(request, pk, template_name='waterevent/region_home.html'):
    region = get_object_or_404(Region, pk=pk)
    if request.method == 'POST':
        region.delete()
        return redirect('waterevent:regionlist')
    return render(request, template_name, {'object': region})


def region_detail(request):
    if request.method == 'POST':
        regionId = str(request.POST.get('tag'))
        region = Region.objects.raw('Select * from Region where regionId =  %s', [regionId])
        context = {'region': region}
        template = loader.get_template('waterevent/region_detail.html')
        return HttpResponse(template.render(context, request))

def RegionView(request, regionId):
    region = get_object_or_404(Location, pk=regionId)
    context = {'region': region}
    return render(request, 'waterevent/region_detail.html', context)

    region = get_object_or_404(Location, pk = locationId)
    context = {'region':region}
    return render(request, 'waterevent/detail.html', context)

#====================pipe ======================
def pipe(request):
    pipe = Pipe.objects.all()
    context = {'pipe': pipe}
    return render(request, 'waterevent/pipe_home.html', context)


class PipeCreate(ModelForm):
    class Meta:
        model = Pipe
        fields = ['pipeId', 'capacity', 'sourcelocation', 'sensorId']

def Pipe_create(request, template_name='waterevent/pipe_form.html'):
    form = PipeCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('waterevent:pipelist')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def PipeList(request):
    pipes = Pipe.objects.all()
    context = {'pipe': pipes}
    return render(request, 'waterevent/pipe_home.html', context)

def pipe_detail(request):
    if request.method == 'POST':
        pipeId = (request.POST.get('tag'))
        pipe = Pipe.objects.raw('Select * from Pipe where pipeId =  %s', [pipeId])
        context = {'pipe': pipe}
        template = loader.get_template('waterevent/pipe_detail.html')
        return HttpResponse(template.render(context, request))

def Pipe_Update(request,pk, template_name='waterevent/pipe_form.html'):
    #pipeId = (request.POST.get('tag1'))
    pipe = get_object_or_404(Pipe, pk=pk)
    form = PipeCreate(request.POST or None, instance=pipe)
    if form.is_valid():
        form.save()
        return redirect('waterevent:pipelist')
    ctx = {"form": form}
    return render(request,'waterevent/pipe_form.html', ctx)


def Pipe_Delete(request):
    pk = (request.POST.get('tag2'))
    pipe = get_object_or_404(Pipe, pk=pk)
    if request.method =='POST':
        pipe.delete()
        return redirect('waterevent:index')
    return render(request,'waterevent/pipe_form',{'object':pipe})

#====================integration ======================
def integration(request):
    integration = WatershedPipe.objects.all()
    context = {'integration': integration}
    return render(request, 'waterevent/integration_home.html', context)

def IntegrationList(request):
    #integration = WatershedPipe.objects.using('Integration').all()
    integration = WatershedPipe.objects.raw('Select * from WatershedPipe')
    context = {'integration': integration}
    template = loader.get_template('waterevent/integration_home.html')
    return HttpResponse(template.render(context, request))


def integration_detail(request, template='waterevent/integration_detail.html'):
    if request.method == 'POST':
        connectionID = (request.POST.get('tag'))
        integration = WatershedPipe.objects.raw('Select * from WatershedPipe where connectionID = %s',[connectionID])
        context = {'integration': integration}
        #template = loader.get_template('waterevent/integration_detail.html')
        #return HttpResponse(template.render(context, request))
        return render(request, template, context)

class connectionCreate(ModelForm):
    # connectionID = forms.CharField()
    # pipeID = forms.ChoiceField(choices=Pipe.objects.values())
    # watershedID =  forms.ChoiceField(choices=Watershed.objects.values())
    class Meta:
        model = WatershedPipe
        fields = ['connectionID', 'pipeID', 'watershedID']

def Integration_create(request, template_name='waterevent/integration_add.html'):
    form = connectionCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('waterevent:integrationlist')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def Integration_Delete(request, pk, template_name = 'waterevent/integration_detail.html'):
    #pk = (request.POST.get('tag2'))
    integration = get_object_or_404(WatershedPipe, pk=pk)
    if request.method == 'POST':
        integration.delete()
        return redirect('waterevent:integrationlist')
    return render(request, 'waterevent/integration_add.html', {'object': integration})



def Integration_Update(request, pk, template_name='waterevent/integration_add.html'):
    integration = get_object_or_404(WatershedPipe, pk=pk)
    form = connectionCreate(request.POST or None, instance=integration)
    if form.is_valid():
        form.save()
        return redirect('waterevent:integrationlist')
    ctx = {"form": form}
    return render(request, template_name, ctx)