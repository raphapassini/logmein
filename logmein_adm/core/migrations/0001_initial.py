# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Projects'
        db.create_table(u'core_projects', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('timezone', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'core', ['Projects'])


    def backwards(self, orm):
        # Deleting model 'Projects'
        db.delete_table(u'core_projects')


    models = {
        u'core.projects': {
            'Meta': {'object_name': 'Projects'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['core']