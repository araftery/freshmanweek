# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Auditioner.email'
        db.add_column(u'talentshow_auditioner', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='test@gmail.com', unique=True, max_length=254),
                      keep_default=False)

        # Adding field 'Auditioner.phone'
        db.add_column(u'talentshow_auditioner', 'phone',
                      self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Auditioner.description'
        db.add_column(u'talentshow_auditioner', 'description',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=500),
                      keep_default=False)

        # Adding field 'Auditioner.time_registered'
        db.add_column(u'talentshow_auditioner', 'time_registered',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Auditioner.reminder_email'
        db.add_column(u'talentshow_auditioner', 'reminder_email',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Auditioner.reminder_text'
        db.add_column(u'talentshow_auditioner', 'reminder_text',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Auditioner.email'
        db.delete_column(u'talentshow_auditioner', 'email')

        # Deleting field 'Auditioner.phone'
        db.delete_column(u'talentshow_auditioner', 'phone')

        # Deleting field 'Auditioner.description'
        db.delete_column(u'talentshow_auditioner', 'description')

        # Deleting field 'Auditioner.time_registered'
        db.delete_column(u'talentshow_auditioner', 'time_registered')

        # Deleting field 'Auditioner.reminder_email'
        db.delete_column(u'talentshow_auditioner', 'reminder_email')

        # Deleting field 'Auditioner.reminder_text'
        db.delete_column(u'talentshow_auditioner', 'reminder_text')


    models = {
        u'talentshow.auditioner': {
            'Meta': {'object_name': 'Auditioner'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'reminder_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reminder_text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_registered': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'talentshow.auditionsession': {
            'Meta': {'object_name': 'AuditionSession'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'talentshow.auditionslot': {
            'Meta': {'object_name': 'AuditionSlot'},
            'auditioner': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['talentshow.Auditioner']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['talentshow.AuditionSession']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['talentshow']