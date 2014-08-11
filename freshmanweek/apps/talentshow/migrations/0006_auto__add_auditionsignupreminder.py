# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AuditionSignUpReminder'
        db.create_table(u'talentshow_auditionsignupreminder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
        ))
        db.send_create_signal(u'talentshow', ['AuditionSignUpReminder'])


    def backwards(self, orm):
        # Deleting model 'AuditionSignUpReminder'
        db.delete_table(u'talentshow_auditionsignupreminder')


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
            'secret': ('django.db.models.fields.CharField', [], {'default': "'GJTQRPH5O3EJZADG9GD7QVI0J9HWL4'", 'unique': 'True', 'max_length': '40'}),
            'sent_reminder_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sent_reminder_text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sent_slot_reminder_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_registered': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'talentshow.auditionsession': {
            'Meta': {'object_name': 'AuditionSession'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'talentshow.auditionsignupreminder': {
            'Meta': {'object_name': 'AuditionSignUpReminder'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'talentshow.auditionslot': {
            'Meta': {'object_name': 'AuditionSlot'},
            'auditioner': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['talentshow.Auditioner']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['talentshow.AuditionSession']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['talentshow']