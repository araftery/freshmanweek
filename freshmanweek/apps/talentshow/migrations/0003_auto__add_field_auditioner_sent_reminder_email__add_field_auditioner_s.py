# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Auditioner.sent_reminder_email'
        db.add_column(u'talentshow_auditioner', 'sent_reminder_email',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Auditioner.sent_reminder_text'
        db.add_column(u'talentshow_auditioner', 'sent_reminder_text',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Auditioner.sent_slot_reminder_email'
        db.add_column(u'talentshow_auditioner', 'sent_slot_reminder_email',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'AuditionSlot.auditioner'
        db.alter_column(u'talentshow_auditionslot', 'auditioner_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['talentshow.Auditioner'], unique=True, null=True, on_delete=models.SET_NULL))

    def backwards(self, orm):
        # Deleting field 'Auditioner.sent_reminder_email'
        db.delete_column(u'talentshow_auditioner', 'sent_reminder_email')

        # Deleting field 'Auditioner.sent_reminder_text'
        db.delete_column(u'talentshow_auditioner', 'sent_reminder_text')

        # Deleting field 'Auditioner.sent_slot_reminder_email'
        db.delete_column(u'talentshow_auditioner', 'sent_slot_reminder_email')


        # Changing field 'AuditionSlot.auditioner'
        db.alter_column(u'talentshow_auditionslot', 'auditioner_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['talentshow.Auditioner'], unique=True, null=True))

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