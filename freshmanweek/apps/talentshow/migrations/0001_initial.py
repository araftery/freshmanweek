# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Auditioner'
        db.create_table(u'talentshow_auditioner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'talentshow', ['Auditioner'])

        # Adding model 'AuditionSession'
        db.create_table(u'talentshow_auditionsession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'talentshow', ['AuditionSession'])

        # Adding model 'AuditionSlot'
        db.create_table(u'talentshow_auditionslot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('auditioner', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['talentshow.Auditioner'], unique=True, null=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['talentshow.AuditionSession'])),
        ))
        db.send_create_signal(u'talentshow', ['AuditionSlot'])


    def backwards(self, orm):
        # Deleting model 'Auditioner'
        db.delete_table(u'talentshow_auditioner')

        # Deleting model 'AuditionSession'
        db.delete_table(u'talentshow_auditionsession')

        # Deleting model 'AuditionSlot'
        db.delete_table(u'talentshow_auditionslot')


    models = {
        u'talentshow.auditioner': {
            'Meta': {'object_name': 'Auditioner'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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