# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    eventid = models.IntegerField(db_column='eventId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Event'


class Happen(models.Model):
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionId')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Happen'


class Location(models.Model):
    locationid = models.IntegerField(db_column='locationId', primary_key=True)  # Field name made lowercase.
    locname = models.CharField(db_column='locName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loclatitude = models.FloatField(db_column='locLatitude', blank=True, null=True)  # Field name made lowercase.
    loclongitude = models.FloatField(db_column='locLongitude', blank=True, null=True)  # Field name made lowercase.
    sensorid = models.ForeignKey('Sensor', on_delete=models.CASCADE, db_column='sensorId', blank=True, null=True)  # Field name made lowercase.
    regionid = models.ForeignKey('Region', on_delete=models.CASCADE, db_column='regionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'


class Observreport(models.Model):
    observid = models.IntegerField(db_column='observId', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    observname = models.CharField(db_column='observName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    overflow = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ObservReport'


class Pipe(models.Model):
    pipeid = models.IntegerField(db_column='pipeId', primary_key=True)  # Field name made lowercase.
    capacity = models.FloatField(blank=True, null=True)
    sourcelocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='sourcelocation', blank=True, null=True)
    endlocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='endlocation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pipe'


class Region(models.Model):
    regionid = models.IntegerField(db_column='regionId', primary_key=True)  # Field name made lowercase.
    regionname = models.CharField(db_column='regionName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Region'


class Sensor(models.Model):
    sensorid = models.IntegerField(db_column='sensorId', primary_key=True)  # Field name made lowercase.
    volume = models.FloatField(blank=True, null=True)
    phlevel = models.IntegerField(db_column='phLevel', blank=True, null=True)  # Field name made lowercase.
    contaminantlevel = models.FloatField(db_column='contaminantLevel', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    observid = models.ForeignKey(Observreport, models.DO_NOTHING, db_column='observId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sensor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Pipeline(models.Model):
    pipelineid = models.IntegerField(db_column='pipelineId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pipeline'


class Student(models.Model):
    idstudent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class WatereventHappen(models.Model):
    regionid = models.IntegerField(db_column='regionId')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waterevent_happen'


class WatereventLocation(models.Model):
    locname = models.CharField(db_column='locName', max_length=20)  # Field name made lowercase.
    loclatitude = models.FloatField(db_column='locLatitude')  # Field name made lowercase.
    loclongitude = models.IntegerField(db_column='locLongitude')  # Field name made lowercase.
    locationid = models.IntegerField(db_column='locationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waterevent_location'


class WatereventObservreport(models.Model):
    observid = models.IntegerField(db_column='observId')  # Field name made lowercase.
    date = models.DateField()
    observname = models.CharField(db_column='observName', max_length=20)  # Field name made lowercase.
    overflow = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'waterevent_observreport'


class WatereventPipe(models.Model):
    pipeid = models.IntegerField(db_column='pipeId')  # Field name made lowercase.
    capacity = models.FloatField()
    sourcelocation = models.IntegerField(db_column='sourceLocation')  # Field name made lowercase.
    endlocation = models.IntegerField(db_column='endLocation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waterevent_pipe'


class WatereventRegion(models.Model):
    regionid = models.IntegerField(db_column='regionId')  # Field name made lowercase.
    regionname = models.CharField(db_column='regionName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waterevent_region'


class WatereventSensor(models.Model):
    sensorid = models.IntegerField(db_column='sensorId')  # Field name made lowercase.
    volume = models.FloatField()
    phlevel = models.IntegerField(db_column='phLevel')  # Field name made lowercase.
    contaminantlevel = models.FloatField(db_column='contaminantLevel')  # Field name made lowercase.
    date = models.DateField()
    observid = models.IntegerField(db_column='observId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waterevent_sensor'
