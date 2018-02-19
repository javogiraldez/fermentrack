# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-14 02:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeerLogPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_temp', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('beer_set', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('beer_ann', models.CharField(max_length=255, null=True)),
                ('fridge_temp', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('fridge_set', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('fridge_ann', models.CharField(max_length=255, null=True)),
                ('room_temp', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('state', models.IntegerField(choices=[(0, 'IDLE'), (1, 'STATE_OFF'), (2, 'DOOR_OPEN'), (3, 'HEATING'), (4, 'COOLING'), (5, 'WAITING_TO_COOL'), (6, 'WAITING_TO_HEAT'), (7, 'WAITING_FOR_PEAK_DETECT'), (8, 'COOLING_MIN_TIME'), (9, 'HEATING_MIN_TIME')], default=0)),
                ('log_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('temp_format', models.CharField(choices=[('C', 'Celsius'), ('F', 'Fahrenheit')], default='C', max_length=1)),
            ],
            options={
                'ordering': ['log_time'],
                'verbose_name': 'Beer Log Point',
                'managed': False,
                'verbose_name_plural': 'Beer Log Points',
            },
        ),
        migrations.CreateModel(
            name='PinDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=16)),
                ('type', models.CharField(default='', max_length=8)),
                ('pin', models.IntegerField(default=-1)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=16)),
                ('device_index', models.IntegerField(default=-1)),
                ('type', models.IntegerField(default=0)),
                ('chamber', models.IntegerField(default=0)),
                ('beer', models.IntegerField(default=0)),
                ('device_function', models.IntegerField(choices=[(0, 'NONE'), (1, 'Chamber Door'), (2, 'Heating Relay'), (3, 'Cooling Relay'), (4, 'Chamber Light'), (5, 'Chamber Temp'), (6, 'Room (outside) Temp'), (7, 'Chamber Fan'), (9, 'Beer Temp')], default=0)),
                ('hardware', models.IntegerField(choices=[(0, 'NONE'), (1, 'PIN'), (2, 'ONEWIRE_TEMP'), (3, 'ONEWIRE_2413'), (4, 'ONEWIRE_2408/Valve')], default=2)),
                ('deactivated', models.IntegerField(default=0)),
                ('pin', models.IntegerField(default=0)),
                ('calibrate_adjust', models.FloatField(default=0.0)),
                ('pio', models.IntegerField(default=None, null=True)),
                ('invert', models.IntegerField(choices=[(0, 'Not Inverted'), (1, 'Inverted')], default=1)),
            ],
            options={
                'verbose_name': 'Sensor Device',
                'managed': False,
                'verbose_name_plural': 'Sensor Devices',
            },
        ),
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('format', models.CharField(default='F', max_length=1)),
                ('model_version', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='BrewPiDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(help_text='Nombre único para el dispositivo', max_length=48, unique=True)),
                ('temp_format', models.CharField(choices=[('C', 'Celsius'), ('F', 'Fahrenheit')], default='C', help_text='Unidad de temperatura', max_length=1)),
                ('data_point_log_interval', models.IntegerField(choices=[(10, '10 Segundos'), (30, '30 Segundos'), (60, '1 Minuto'), (120, '2 Minutos'), (300, '5 Minutos'), (600, '10 Minutos'), (1800, '30 Minutos'), (3600, '1 Hora')], default=30, help_text='Tiempo entre tomas de temperatura')),
                ('useInetSocket', models.BooleanField(default=False, help_text='Usar o no una conexión de internet (en lugar de local)')),
                ('socketPort', models.IntegerField(default=2222, help_text='Socket a usar (sólo se usa si useInetSocket es "Si")', validators=[django.core.validators.MinValueValidator(10, 'El puerto de ser 10 o mayor'), django.core.validators.MaxValueValidator(65535, 'El puerto debe ser 65535 o menor')])),
                ('socketHost', models.CharField(default='localhost', help_text='Interfaz para vincular el socket (sólo si useInetSocket es "Si")', max_length=128)),
                ('logging_status', models.CharField(choices=[('active', 'Active'), ('paused', 'Paused'), ('stopped', 'Stopped')], default='stopped', help_text='Estado de logging de Datos', max_length=10)),
                ('serial_port', models.CharField(default='auto', help_text='Puerto Serial donde el dispositivo BrewPi es conectado', max_length=255)),
                ('serial_alt_port', models.CharField(default='None', help_text='Puerto Serial Alternativo donde el dispositivo BrewPi es conectado (??)', max_length=255)),
                ('board_type', models.CharField(choices=[('uno', 'Arduino Uno (o compatible)'), ('esp8266', 'ESP8266'), ('leonardo', 'Arduino Leonardo'), ('core', 'Core'), ('photon', 'Photon')], default='uno', help_text='Tipo de placa a donde se conecta BrewPi', max_length=10)),
                ('status', models.CharField(choices=[('active', 'Active, administrado por Circus'), ('unmanaged', 'Active, NO administrado por Circus'), ('disabled', 'Explicitamente desconectado, no será ejecutado'), ('updating', 'Desconectado, pendiente de actualización')], default='active', max_length=15)),
                ('socket_name', models.CharField(default='BEERSOCKET', help_text='Nombre del archivo basado en socket (Sólo usado si useInetSocket is "No")', max_length=25)),
                ('connection_type', models.CharField(choices=[('serial', 'Serial (Arduino y otros)'), ('wifi', 'WiFi (ESP8266)')], default='serial', help_text='Tipo de conexión entre la Raspberry Pi el dispositivo', max_length=15)),
                ('wifi_host', models.CharField(default='None', help_text='mDNS Nombre del host o dirección IP para dispositivos conectados por WIFI (sólo usado si connection_type es wifi)', max_length=40)),
                ('wifi_port', models.IntegerField(default=23, help_text='El socket de Internet a usar (sólo usado si connection_type es wifi)', validators=[django.core.validators.MinValueValidator(10, 'Port must be 10 or higher'), django.core.validators.MaxValueValidator(65535, 'Port must be 65535 or lower')])),
                ('time_profile_started', models.DateTimeField(blank=True, default=None, null=True)),
                ('active_beer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Beer')),
            ],
            options={
                'verbose_name': 'BrewPi Device',
                'verbose_name_plural': 'BrewPi Devices',
            },
        ),
        migrations.CreateModel(
            name='FermentationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Pending Delete')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='FermentationProfilePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttl', models.DurationField(help_text='Hora en la que creemos que llegará a esa temperatura')),
                ('temperature_setting', models.DecimalField(decimal_places=2, help_text='La temperatura a la que debería estar la cerveza si TTL se ha pasado', max_digits=5, null=True)),
                ('temp_format', models.CharField(default='F', max_length=1)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.FermentationProfile')),
            ],
        ),
        migrations.CreateModel(
            name='NewControlConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempFormat', models.CharField(default='C', max_length=1)),
                ('heater1_kp', models.FloatField(help_text='Actuator output in % = Kp * input error')),
                ('heater1_ti', models.IntegerField()),
                ('heater1_td', models.IntegerField()),
                ('heater1_infilt', models.IntegerField()),
                ('heater1_dfilt', models.IntegerField()),
                ('heater2_kp', models.FloatField()),
                ('heater2_ti', models.IntegerField()),
                ('heater2_td', models.IntegerField()),
                ('heater2_infilt', models.IntegerField()),
                ('heater2_dfilt', models.IntegerField()),
                ('cooler_kp', models.FloatField()),
                ('cooler_ti', models.IntegerField()),
                ('cooler_td', models.IntegerField()),
                ('cooler_infilt', models.IntegerField()),
                ('cooler_dfilt', models.IntegerField()),
                ('beer2fridge_kp', models.FloatField()),
                ('beer2fridge_ti', models.IntegerField()),
                ('beer2fridge_td', models.IntegerField()),
                ('beer2fridge_infilt', models.IntegerField()),
                ('beer2fridge_dfilt', models.IntegerField()),
                ('beer2fridge_pidMax', models.FloatField()),
                ('minCoolTime', models.IntegerField()),
                ('minCoolIdleTime', models.IntegerField()),
                ('heater1PwmPeriod', models.IntegerField()),
                ('heater2PwmPeriod', models.IntegerField()),
                ('coolerPwmPeriod', models.IntegerField()),
                ('mutexDeadTime', models.IntegerField()),
                ('preset_name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OldControlConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempSetMin', models.FloatField(help_text="The fridge and beer temperatures cannot go below this value. Units are specified by 'Temperature format' below.", verbose_name='Min Temperature')),
                ('tempSetMax', models.FloatField(help_text="The fridge and beer temperatures cannot go above this value. Units are specified by 'Temperature format' below.", verbose_name='Max Temperature')),
                ('Kp', models.FloatField(help_text='The beer temperature error is multiplied by Kp to give the proportional of the PID value', verbose_name='PID: Kp')),
                ('Ki', models.FloatField(help_text='When the integral is active, the error is added to the integral every 30 sec. The result is multiplied by Ki to give the integral part.', verbose_name='PID: Ki')),
                ('Kd', models.FloatField(help_text='The derivative of the beer temperature is multiplied by Kd to give the derivative part of the PID value', verbose_name='PID: Kd')),
                ('pidMax', models.FloatField(help_text='Defines the maximum difference between the beer temp setting and fridge temp setting. The fridge setting will be clipped to this range.', verbose_name='PID: maximum')),
                ('iMaxErr', models.FloatField(help_text='The integral is only active when the temperature is close to the target temperature. This is the maximum error for which the integral is active.', verbose_name='Integrator: Max temp error C')),
                ('idleRangeH', models.FloatField(help_text='When the fridge temperature is within this range, it will not heat or cool, regardless of other settings', verbose_name='Temperature idle range top')),
                ('idleRangeL', models.FloatField(help_text='When the fridge temperature is within this range, it will not heat or cool, regardless of other settings', verbose_name='Temperature idle range bottom')),
                ('heatTargetH', models.FloatField(help_text='When the overshoot lands under this value, the peak is within the target range and the estimator is not adjusted', verbose_name='Heating target upper bound')),
                ('heatTargetL', models.FloatField(help_text='When the overshoot lands above this value, the peak is within the target range and the estimator is not adjusted', verbose_name='Heating target lower bound')),
                ('coolTargetH', models.FloatField(help_text='When the overshoot lands under this value, the peak is within the target range and the estimator is not adjusted', verbose_name='Cooling target upper bound')),
                ('coolTargetL', models.FloatField(help_text='When the overshoot lands above this value, the peak is within the target range and the estimator is not adjusted', verbose_name='Cooling target lower bound')),
                ('maxHeatTimeForEst', models.IntegerField(help_text='The time the fridge has been heating is used to estimate overshoot. This is the maximum time that is taken into account.', verbose_name='Maximum time in seconds for heating overshoot estimator')),
                ('maxCoolTimeForEst', models.IntegerField(help_text='Maximum time the fridge has been cooling is used to estimate overshoot. This is the maximum time that is taken into account.', verbose_name='Maximum time in seconds for cooling overshoot estimator')),
                ('beerFastFilt', models.IntegerField(help_text='The beer fast filter is used for display and data logging. More filtering gives a smoother line but also more delay.', verbose_name='Beer fast filter delay time')),
                ('beerSlowFilt', models.IntegerField(help_text='The beer slow filter is used for the control algorithm. The fridge temperature setting is calculated from this filter. Because a small difference in beer temperature cases a large adjustment in the fridge temperature, more smoothing is needed.', verbose_name='Beer slow filter delay time')),
                ('beerSlopeFilt', models.IntegerField(help_text='The slope is calculated every 30 sec and fed to this filter. More filtering means a smoother fridge setting.', verbose_name='Beer slope filter delay time')),
                ('fridgeFastFilt', models.IntegerField(help_text='The fridge fast filter is used for on-off control, display, and logging. It needs to have a small delay.', verbose_name='Fridge fast filter delay time')),
                ('fridgeSlowFilt', models.IntegerField(help_text='The fridge slow filter is used for peak detection to adjust the overshoot estimators. More smoothing is needed to prevent small fluctuations from being recognized as peaks.', verbose_name='Fridge slow filter delay time')),
                ('fridgeSlopeFilt', models.IntegerField(help_text='Fridge slope filter is not used in this revision of the firmware.', verbose_name='Fridge slope filter delay time')),
                ('lah', models.IntegerField(choices=[(1, 'YES'), (0, 'No')], default=0, help_text='If set to yes the chamber light (if assigned a pin) will be used in place of the heat pin', verbose_name='Using light as heater?')),
                ('hs', models.IntegerField(choices=[(1, 'YES'), (0, 'No')], default=0, help_text='If this option is set to yes, the rotary encoder will use half steps', verbose_name='Use half steps for rotary encoder?')),
                ('tempFormat', models.CharField(choices=[('F', 'Fahrenheit'), ('C', 'Celsius')], default='F', max_length=1, verbose_name='Temperature format')),
                ('preset_name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='brewpidevice',
            name='active_profile',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FermentationProfile'),
        ),
        migrations.AddField(
            model_name='beer',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.BrewPiDevice'),
        ),
    ]
