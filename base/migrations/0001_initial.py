# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Setting'
        db.create_table(u'base_setting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'base', ['Setting'])

        # Adding model 'Menu'
        db.create_table(u'base_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'base', ['Menu'])

        # Adding model 'Partners'
        db.create_table(u'base_partners', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'base', ['Partners'])

        # Adding model 'News'
        db.create_table(u'base_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 23, 0, 0), max_length=255)),
            ('short_descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descr', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'base', ['News'])

        # Adding model 'NewsImages'
        db.create_table(u'base_newsimages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.News'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'base', ['NewsImages'])

        # Adding model 'Recipe'
        db.create_table(u'base_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 23, 0, 0), max_length=255)),
            ('short_descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ingredients_prefix', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('instruction', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'base', ['Recipe'])

        # Adding model 'RecipeIngredients'
        db.create_table(u'base_recipeingredients', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Recipe'])),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'base', ['RecipeIngredients'])

        # Adding model 'RecipeImages'
        db.create_table(u'base_recipeimages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipeimages', to=orm['base.Recipe'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'base', ['RecipeImages'])

        # Adding model 'ProductCategory'
        db.create_table(u'base_productcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'base', ['ProductCategory'])

        # Adding model 'Product'
        db.create_table(u'base_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.ProductCategory'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('composition', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('calories', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('proteins', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fats', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('carbs', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('storage', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'base', ['Product'])

        # Adding model 'ProductImages'
        db.create_table(u'base_productimages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='productimages', to=orm['base.Product'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'base', ['ProductImages'])


    def backwards(self, orm):
        # Deleting model 'Setting'
        db.delete_table(u'base_setting')

        # Deleting model 'Menu'
        db.delete_table(u'base_menu')

        # Deleting model 'Partners'
        db.delete_table(u'base_partners')

        # Deleting model 'News'
        db.delete_table(u'base_news')

        # Deleting model 'NewsImages'
        db.delete_table(u'base_newsimages')

        # Deleting model 'Recipe'
        db.delete_table(u'base_recipe')

        # Deleting model 'RecipeIngredients'
        db.delete_table(u'base_recipeingredients')

        # Deleting model 'RecipeImages'
        db.delete_table(u'base_recipeimages')

        # Deleting model 'ProductCategory'
        db.delete_table(u'base_productcategory')

        # Deleting model 'Product'
        db.delete_table(u'base_product')

        # Deleting model 'ProductImages'
        db.delete_table(u'base_productimages')


    models = {
        u'base.menu': {
            'Meta': {'ordering': "['order']", 'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'base.news': {
            'Meta': {'ordering': "['-date']", 'object_name': 'News'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 23, 0, 0)', 'max_length': '255'}),
            'descr': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'base.newsimages': {
            'Meta': {'object_name': 'NewsImages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.News']"})
        },
        u'base.partners': {
            'Meta': {'object_name': 'Partners'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'base.product': {
            'Meta': {'ordering': "['order']", 'object_name': 'Product'},
            'calories': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'carbs': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.ProductCategory']"}),
            'composition': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fats': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'proteins': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'storage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'base.productcategory': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'base.productimages': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProductImages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'productimages'", 'to': u"orm['base.Product']"})
        },
        u'base.recipe': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Recipe'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 23, 0, 0)', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients_prefix': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'base.recipeimages': {
            'Meta': {'object_name': 'RecipeImages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipeimages'", 'to': u"orm['base.Recipe']"})
        },
        u'base.recipeingredients': {
            'Meta': {'ordering': "['-order']", 'object_name': 'RecipeIngredients'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Recipe']"}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'base.setting': {
            'Meta': {'object_name': 'Setting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['base']