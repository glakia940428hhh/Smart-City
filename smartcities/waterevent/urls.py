"""smartcities URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from. import views

#app_name="event"

urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^event',views.EventList,name="eventlist"),

    url(r'^add-event',views.Event_create,name="add-event"),
    url(r'^detail/(?P<pk>\d+)',views.detail,name="detail"),
    url(r'^update/(?P<pk>\d+)$', views.EventUpdate, name="detail-update"),
    url(r'^delete/(?P<pk>\d+)$', views.EventDelete, name="detail-delete"),

    url(r'^map',views.map, name="map"),

    url(r'^report/$', views.ReportList, name="reportlist"),
    url(r'^add-report', views.Report_create, name="add-report"),
    url(r'^report/report_detail', views.report_detail, name="report_detail"),
    url(r'^report/update/(?P<pk>\d+)$', views.Report_Update, name="report_detail-update"),
    url(r'^report/delete/(?P<pk>\d+)$', views.Report_Delete, name="report_detail-delete"),

    url(r'^sensor/$', views.SensorList, name="sensorlist"),
    url(r'^add-sensor', views.Sensor_create, name="add-sensor"),
    url(r'^sensor/sensor_detail', views.sensor_detail, name="sensor_detail"),
    url(r'^sensorupdate/(?P<pk>\d+)$', views.SensorUpdate, name="sensor-update"),
    url(r'^sensordelete/(?P<pk>\d+)$', views.SensorDelete, name="sensor-delete"),

    url(r'^location/$', views.LocationList, name="locationlist"),
    url(r'^add-location', views.Location_create, name="add-location"),
    url(r'^location/location_detail', views.location_detail, name="location_detail"),
    url(r'^location/update/(?P<pk>\d+)$', views.Location_Update, name="location_detail-update"),
    url(r'^location/delete/(?P<pk>\d+)$', views.Location_Delete, name="location_detail-delete"),

    url(r'^region/$', views.RegionList, name="regionlist"),
    url(r'^add-region', views.Region_create, name="add-region"),
    url(r'^region/region_detail', views.region_detail, name="region_detail"),
    url(r'^region/update/(?P<pk>\d+)$', views.Region_Update, name="region_detail-update"),
    url(r'^region/delete/(?P<pk>\w+)$', views.Region_Delete, name="region_detail-delete"),

    #=====pipe============
    url(r'^pipe/$', views.PipeList, name="pipelist"),
    url(r'^add-pipe', views.Pipe_create, name="add-pipe"),
    url(r'^pipe/pipe_detail', views.pipe_detail, name="pipe_detail"),
    url(r'^pipe/update/(?P<pk>\w+)$', views.Pipe_Update, name="pipe-update"),
    url(r'^pipe/delete/$', views.Pipe_Delete, name="pipe-delete"),

    # ====connection=======
    url(r'^integration/$', views.IntegrationList, name="integrationlist"),
    url(r'^integration/integration_detail', views.integration_detail, name="integration_detail"),
    url(r'^integration/integration_add', views.Integration_create, name="integration_add"),
    url(r'^integration/update/(?P<pk>\w+)$', views.Integration_Update, name="integration-update"),
    url(r'^integration/delete/(?P<pk>\w+)$', views.Integration_Delete, name="integration-delete"),
]
