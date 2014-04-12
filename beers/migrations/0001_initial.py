# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Glassware'
        db.create_table(u'beers_glassware', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('glass_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'beers', ['Glassware'])

        # Adding model 'BeerStyle'
        db.create_table(u'beers_beerstyle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('category_number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('subcategory', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('glassware', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beers.Glassware'])),
            ('og_min', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('og_max', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('fg_min', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('fg_max', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('abv_min', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('abv_max', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('ibu_min', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ibu_max', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('srm_min', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('srm_max', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
        ))
        db.send_create_signal(u'beers', ['BeerStyle'])

        # Adding model 'Beer'
        db.create_table(u'beers_beer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beers.BeerStyle'])),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('og_estimated', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('fg_estimated', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('srm_estimated', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('ibu_estimated', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'beers', ['Beer'])

        # Adding model 'SrmRgb'
        db.create_table(u'beers_srmrgb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('srm', self.gf('django.db.models.fields.DecimalField')(default=0, unique=True, max_digits=3, decimal_places=1)),
            ('rgb', self.gf('django.db.models.fields.CharField')(max_length=13)),
        ))
        db.send_create_signal(u'beers', ['SrmRgb'])


    def backwards(self, orm):
        # Deleting model 'Glassware'
        db.delete_table(u'beers_glassware')

        # Deleting model 'BeerStyle'
        db.delete_table(u'beers_beerstyle')

        # Deleting model 'Beer'
        db.delete_table(u'beers_beer')

        # Deleting model 'SrmRgb'
        db.delete_table(u'beers_srmrgb')


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
            'Meta': {'object_name': 'BeerStyle'},
            'abv_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'abv_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'category_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fg_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'fg_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'glassware': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.Glassware']"}),
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
            'glass_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        u'beers.srmrgb': {
            'Meta': {'object_name': 'SrmRgb'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rgb': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'srm': ('django.db.models.fields.DecimalField', [], {'default': '0', 'unique': 'True', 'max_digits': '3', 'decimal_places': '1'})
        }
    }

    complete_apps = ['beers']