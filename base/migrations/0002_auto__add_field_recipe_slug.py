# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.slug'
        db.add_column(u'base_recipe', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recipe.slug'
        db.delete_column(u'base_recipe', 'slug')


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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
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