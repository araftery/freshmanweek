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
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'talentshow', ['AuditionSignUpReminder'])

        # Adding field 'Auditioner.email'
        db.add_column(u'talentshow_auditioner', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='noemail@gmail.com', unique=True, max_length=254),
                      keep_default=False)

        # Adding field 'Auditioner.phone'
        db.add_column(u'talentshow_auditioner', 'phone',
                      self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Auditioner.description'
        db.add_column(u'talentshow_auditioner', 'description',
                      self.gf('django.db.models.fields.CharField')(default='No description', max_length=500),
                      keep_default=False)

        # Adding field 'Auditioner.props_info'
        db.add_column(u'talentshow_auditioner', 'props_info',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Auditioner.time_registered'
        db.add_column(u'talentshow_auditioner', 'time_registered',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 8, 21, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Auditioner.reminder_email'
        db.add_column(u'talentshow_auditioner', 'reminder_email',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Auditioner.reminder_text'
        db.add_column(u'talentshow_auditioner', 'reminder_text',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

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
        # Deleting model 'AuditionSignUpReminder'
        db.delete_table(u'talentshow_auditionsignupreminder')

        # Deleting field 'Auditioner.email'
        db.delete_column(u'talentshow_auditioner', 'email')

        # Deleting field 'Auditioner.phone'
        db.delete_column(u'talentshow_auditioner', 'phone')

        # Deleting field 'Auditioner.description'
        db.delete_column(u'talentshow_auditioner', 'description')

        # Deleting field 'Auditioner.props_info'
        db.delete_column(u'talentshow_auditioner', 'props_info')

        # Deleting field 'Auditioner.time_registered'
        db.delete_column(u'talentshow_auditioner', 'time_registered')

        # Deleting field 'Auditioner.reminder_email'
        db.delete_column(u'talentshow_auditioner', 'reminder_email')

        # Deleting field 'Auditioner.reminder_text'
        db.delete_column(u'talentshow_auditioner', 'reminder_text')

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
            'props_info': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'reminder_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'reminder_text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sent_reminder_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sent_reminder_text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sent_slot_reminder_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_registered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'talentshow.auditionsession': {
            'Meta': {'object_name': 'AuditionSession'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'talentshow.auditionsignupreminder': {
            'Meta': {'object_name': 'AuditionSignUpReminder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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