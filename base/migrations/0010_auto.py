# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field recipes on 'Product'
        m2m_table_name = db.shorten_name(u'base_product_recipes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'base.product'], null=False)),
            ('recipe', models.ForeignKey(orm[u'base.recipe'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'recipe_id'])


    def backwards(self, orm):
        # Removing M2M table for field recipes on 'Product'
        db.delete_table(db.shorten_name(u'base_product_recipes'))


    models = {
        u'base.news': {
            'Meta': {'ordering': "['-date']", 'object_name': 'News'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 7, 0, 0)', 'max_length': '255'}),
            'descr': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'short_descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'base.newsimages': {
            'Meta': {'object_name': 'NewsImages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['base.News']"})
        },
        u'base.product': {
            'Meta': {'ordering': "['order']", 'object_name': 'Product'},
            'calories': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'carbs': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.ProductCategory']"}),
            'composition': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fats': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'proteins': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Recipe']", 'symmetrical': 'False'}),
            'short_descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'storage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'base.productcategory': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'base.productimages': {
            'Meta': {'ordering': "['order']", 'object_name': 'ProductImages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['base.Product']"})
        },
        u'base.recipe': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Recipe'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 7, 0, 0)', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
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
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['base.Recipe']"})
        },
        u'base.recipeingredients': {
            'Meta': {'ordering': "['-order']", 'object_name': 'RecipeIngredients'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ingridients'", 'to': u"orm['base.Recipe']"}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'base.wheretobuy': {
            'Meta': {'ordering': "['order']", 'object_name': 'WhereToBuy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'pos_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['base']