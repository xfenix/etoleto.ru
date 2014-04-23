# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MainSlider'
        db.create_table(u'misc_mainslider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'misc', ['MainSlider'])


    def backwards(self, orm):
        # Deleting model 'MainSlider'
        db.delete_table(u'misc_mainslider')


    models = {
        u'misc.mainslider': {
            'Meta': {'ordering': "['order']", 'object_name': 'MainSlider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['misc']