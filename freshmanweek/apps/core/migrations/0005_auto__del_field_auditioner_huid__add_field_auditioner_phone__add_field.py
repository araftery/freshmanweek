# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Auditioner.huid'
        db.delete_column(u'core_auditioner', 'huid')

        # Adding field 'Auditioner.phone'
        db.add_column(u'core_auditioner', 'phone',
                      self.gf('localflavor.us.models.PhoneNumberField')(default=5555555555, max_length=20),
                      keep_default=False)

        # Adding field 'Auditioner.description'
        db.add_column(u'core_auditioner', 'description',
                      self.gf('django.db.models.fields.CharField')(default='No description', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Auditioner.huid'
        db.add_column(u'core_auditioner', 'huid',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Auditioner.phone'
        db.delete_column(u'core_auditioner', 'phone')

        # Deleting field 'Auditioner.description'
        db.delete_column(u'core_auditioner', 'description')


    models = {
        u'core.auditioner': {
            'Meta': {'object_name': 'Auditioner'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'})
        },
        u'core.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'extra_info': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['core']