# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Setting'
        db.delete_table(u'base_setting')

        # Deleting model 'Menu'
        db.delete_table(u'base_menu')


        # Changing field 'NewsImages.image'
        db.alter_column(u'base_newsimages', 'image', self.gf('base.utils.ImagePreviewField')(max_length=100))

        # Changing field 'Product.image'
        db.alter_column(u'base_product', 'image', self.gf('base.utils.ImagePreviewField')(max_length=100))

        # Changing field 'ProductImages.image'
        db.alter_column(u'base_productimages', 'image', self.gf('base.utils.ImagePreviewField')(max_length=100))

        # Changing field 'WhereToBuy.image'
        db.alter_column(u'base_wheretobuy', 'image', self.gf('base.utils.ImagePreviewField')(max_length=100))

        # Changing field 'RecipeImages.image'
        db.alter_column(u'base_recipeimages', 'image', self.gf('base.utils.ImagePreviewField')(max_length=100))

        # Changing field 'ProductCategory.image'
        db.alter_column(u'base_productcategory', 'image', self.gf('base.utils.ImagePreviewField')(max_length=100))

    def backwards(self, orm):
        # Adding model 'Setting'
        db.create_table(u'base_setting', (
            ('value', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal(u'base', ['Setting'])

        # Adding model 'Menu'
        db.create_table(u'base_menu', (
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'base', ['Menu'])


        # Changing field 'NewsImages.image'
        db.alter_column(u'base_newsimages', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'Product.image'
        db.alter_column(u'base_product', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'ProductImages.image'
        db.alter_column(u'base_productimages', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'WhereToBuy.image'
        db.alter_column(u'base_wheretobuy', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'RecipeImages.image'
        db.alter_column(u'base_recipeimages', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'ProductCategory.image'
        db.alter_column(u'base_productcategory', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'base.news': {
            'Meta': {'ordering': "['-date']", 'object_name': 'News'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 26, 0, 0)', 'max_length': '255'}),
            'descr': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'productimages'", 'to': u"orm['base.Product']"})
        },
        u'base.recipe': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Recipe'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 26, 0, 0)', 'max_length': '255'}),
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
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipeimages'", 'to': u"orm['base.Recipe']"})
        },
        u'base.recipeingredients': {
            'Meta': {'ordering': "['-order']", 'object_name': 'RecipeIngredients'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Recipe']"}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'base.wheretobuy': {
            'Meta': {'ordering': "['order']", 'object_name': 'WhereToBuy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('base.utils.ImagePreviewField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'pos_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['base']