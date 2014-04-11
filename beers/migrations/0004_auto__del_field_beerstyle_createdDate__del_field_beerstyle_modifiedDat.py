# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BeerStyle.createdDate'
        db.delete_column(u'beers_beerstyle', 'createdDate')

        # Deleting field 'BeerStyle.modifiedDate'
        db.delete_column(u'beers_beerstyle', 'modifiedDate')

        # Adding field 'BeerStyle.create_date'
        db.add_column(u'beers_beerstyle', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'BeerStyle.modified_date'
        db.add_column(u'beers_beerstyle', 'modified_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Beer.modifiedDate'
        db.delete_column(u'beers_beer', 'modifiedDate')

        # Deleting field 'Beer.createdDate'
        db.delete_column(u'beers_beer', 'createdDate')

        # Adding field 'Beer.create_date'
        db.add_column(u'beers_beer', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Beer.modified_date'
        db.add_column(u'beers_beer', 'modified_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'Beer.slug'
        db.alter_column(u'beers_beer', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))
        # Deleting field 'Keg.modifiedDate'
        db.delete_column(u'beers_keg', 'modifiedDate')

        # Deleting field 'Keg.createdDate'
        db.delete_column(u'beers_keg', 'createdDate')

        # Adding field 'Keg.create_date'
        db.add_column(u'beers_keg', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Keg.modified_date'
        db.add_column(u'beers_keg', 'modified_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'BeerStyle.createdDate'
        db.add_column(u'beers_beerstyle', 'createdDate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'BeerStyle.modifiedDate'
        db.add_column(u'beers_beerstyle', 'modifiedDate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'BeerStyle.create_date'
        db.delete_column(u'beers_beerstyle', 'create_date')

        # Deleting field 'BeerStyle.modified_date'
        db.delete_column(u'beers_beerstyle', 'modified_date')

        # Adding field 'Beer.modifiedDate'
        db.add_column(u'beers_beer', 'modifiedDate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Beer.createdDate'
        db.add_column(u'beers_beer', 'createdDate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Beer.create_date'
        db.delete_column(u'beers_beer', 'create_date')

        # Deleting field 'Beer.modified_date'
        db.delete_column(u'beers_beer', 'modified_date')


        # Changing field 'Beer.slug'
        db.alter_column(u'beers_beer', 'slug', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=('createdDate',), populate_from='name'))
        # Adding field 'Keg.modifiedDate'
        db.add_column(u'beers_keg', 'modifiedDate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Keg.createdDate'
        db.add_column(u'beers_keg', 'createdDate',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 11, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Keg.create_date'
        db.delete_column(u'beers_keg', 'create_date')

        # Deleting field 'Keg.modified_date'
        db.delete_column(u'beers_keg', 'modified_date')


    models = {
        u'beers.beer': {
            'Meta': {'object_name': 'Beer'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fgEst': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'ibuEst': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ogEst': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'srmEst': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.BeerStyle']"})
        },
        u'beers.beerstyle': {
            'Meta': {'object_name': 'BeerStyle'},
            'abvMax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'abvMin': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'catNum': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fgMax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'fgMin': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'ibuMax': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ibuMin': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'ogMax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'ogMin': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'srmMax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'srmMin': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'})
        },
        u'beers.keg': {
            'Meta': {'object_name': 'Keg'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kegstatus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.KegStatus']"}),
            'kegtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.KegType']"}),
            'label': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'stampedLoc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'stampedOwner': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '4'})
        },
        u'beers.kegstatus': {
            'Meta': {'object_name': 'KegStatus'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'beers.kegtype': {
            'Meta': {'object_name': 'KegType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxamount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'beers.srmrgb': {
            'Meta': {'object_name': 'SrmRgb'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rgb': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'srm': ('django.db.models.fields.DecimalField', [], {'default': '0', 'unique': 'True', 'max_digits': '3', 'decimal_places': '1'})
        },
        u'beers.tap': {
            'Meta': {'object_name': 'Tap'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'beer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.Beer']"}),
            'fgAct': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'ibuAct': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.Keg']"}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'ogAct': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'srmAct': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'})
        }
    }

    complete_apps = ['beers']