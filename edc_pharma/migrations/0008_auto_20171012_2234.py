# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 20:34
from __future__ import unicode_literals

import _socket
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('edc_pharma', '0007_dispensehistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationDefinition',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('short_name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('description', models.CharField(max_length=250)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('category', models.CharField(max_length=20)),
                ('storage_instructions', models.TextField(max_length=200)),
                ('unit', models.CharField(max_length=20)),
                ('milligram', models.CharField(max_length=200)),
                ('number_of_times_per_day', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='dispenseappointment',
            name='timepoint',
        ),
        migrations.RemoveField(
            model_name='dispensehistory',
            name='medications',
        ),
        migrations.RemoveField(
            model_name='dispenseschedule',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='dispenseschedule',
            name='start_date',
        ),
        migrations.AddField(
            model_name='dispenseappointment',
            name='appt_datetime',
            field=models.DateTimeField(db_index=True, default=None, verbose_name='Appointment date and time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dispenseappointment',
            name='appt_reason',
            field=models.CharField(blank=True, help_text='Reason for appointment', max_length=25, verbose_name='Reason for appointment'),
        ),
        migrations.AddField(
            model_name='dispenseappointment',
            name='comment',
            field=models.CharField(blank=True, max_length=250, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='dispenseappointment',
            name='dispense_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Dispense date and time'),
        ),
        migrations.AddField(
            model_name='dispenseappointment',
            name='facility_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dispenseappointment',
            name='visit_code_sequence',
            field=models.IntegerField(blank=True, default=0, help_text='An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)', null=True, verbose_name='Sequence'),
        ),
        migrations.AddField(
            model_name='dispensehistory',
            name='duration',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dispensehistory',
            name='result',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dispensehistory',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Weight in kg'),
        ),
        migrations.AddField(
            model_name='dispenseschedule',
            name='end_datetime',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dispenseschedule',
            name='start_datetime',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dispenseappointment',
            name='is_dispensed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='dispensehistory',
            name='dispense_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Medication',
        ),
        migrations.AddField(
            model_name='dispensehistory',
            name='medication_definition',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='edc_pharma.MedicationDefinition'),
            preserve_default=False,
        ),
    ]
