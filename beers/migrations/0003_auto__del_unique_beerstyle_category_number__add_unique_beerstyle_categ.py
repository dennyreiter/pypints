# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'BeerStyle', fields ['category_number']
        db.delete_unique(u'beers_beerstyle', ['category_number'])

        # Adding unique constraint on 'BeerStyle', fields ['category_number', 'subcategory']
        db.create_unique(u'beers_beerstyle', ['category_number', 'subcategory'])


    def backwards(self, orm):
        # Removing unique constraint on 'BeerStyle', fields ['category_number', 'subcategory']
        db.delete_unique(u'beers_beerstyle', ['category_number', 'subcategory'])

        # Adding unique constraint on 'BeerStyle', fields ['category_number']
        db.create_unique(u'beers_beerstyle', ['category_number'])


    models = {
        u'beers.beer': {
            'Meta': {'object_name': 'Beer'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fg_estimated': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'ibu_estimated': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'og_estimated': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'srm_estimated': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.BeerStyle']"})
        },
        u'beers.beerstyle': {
            'Meta': {'unique_together': "(('category_number', 'subcategory'),)", 'object_name': 'BeerStyle'},
            'abv_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'abv_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'category_number': ('django.db.models.fields.IntegerField', [], {}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fg_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'fg_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'glassware': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['beers.Glassware']"}),
            'ibu_max': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ibu_min': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'og_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'og_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'srm_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'srm_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'subcategory': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'beers.glassware': {
            'Meta': {'object_name': 'Glassware'},
            'glass_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'beers.srmrgb': {
            'Meta': {'object_name': 'SrmRgb'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rgb': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'srm': ('django.db.models.fields.DecimalField', [], {'default': '0', 'unique': 'True', 'max_digits': '3', 'decimal_places': '1'})
        }
    }

    complete_apps = ['beers']