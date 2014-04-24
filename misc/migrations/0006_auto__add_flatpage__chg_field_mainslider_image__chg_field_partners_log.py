# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FlatPage'
        db.create_table(u'misc_flatpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('template_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
        ))
        db.send_create_signal(u'misc', ['FlatPage'])


        # Changing field 'MainSlider.image'
        db.alter_column(u'misc_mainslider', 'image', self.gf('base.misc.ImagePreviewField')(max_length=100))

        # Changing field 'Partners.logo'
        db.alter_column(u'misc_partners', 'logo', self.gf('base.misc.ImagePreviewField')(max_length=100))

        # Changing field 'AboutGalleries.image'
        db.alter_column(u'misc_aboutgalleries', 'image', self.gf('base.misc.ImagePreviewField')(max_length=100))

        # Changing field 'AboutGalleriesImages.image'
        db.alter_column(u'misc_aboutgalleriesimages', 'image', self.gf('base.misc.ImagePreviewField')(max_length=100))

    def backwards(self, orm):
        # Deleting model 'FlatPage'
        db.delete_table(u'misc_flatpage')


        # Changing field 'MainSlider.image'
        db.alter_column(u'misc_mainslider', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'Partners.logo'
        db.alter_column(u'misc_partners', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'AboutGalleries.image'
        db.alter_column(u'misc_aboutgalleries', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'AboutGalleriesImages.image'
        db.alter_column(u'misc_aboutgalleriesimages', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'misc.aboutgalleries': {
            'Meta': {'ordering': "['order']", 'object_name': 'AboutGalleries'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.misc.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'misc.aboutgalleriesimages': {
            'Meta': {'ordering': "['order']", 'object_name': 'AboutGalleriesImages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.misc.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.AboutGalleries']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'misc.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'misc.mainslider': {
            'Meta': {'ordering': "['order']", 'object_name': 'MainSlider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.misc.ImagePreviewField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'misc.partners': {
            'Meta': {'object_name': 'Partners'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'logo': ('base.misc.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['misc']