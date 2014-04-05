# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Beer.notes'
        db.alter_column(u'beers_beer', 'notes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Keg.model'
        db.alter_column(u'beers_keg', 'model', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Keg.make'
        db.alter_column(u'beers_keg', 'make', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Keg.stampedLoc'
        db.alter_column(u'beers_keg', 'stampedLoc', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Keg.stampedOwner'
        db.alter_column(u'beers_keg', 'stampedOwner', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Keg.notes'
        db.alter_column(u'beers_keg', 'notes', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Keg.serial'
        db.alter_column(u'beers_keg', 'serial', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

    def backwards(self, orm):

        # Changing field 'Beer.notes'
        db.alter_column(u'beers_beer', 'notes', self.gf('django.db.models.fields.TextField')(default=' '))

        # Changing field 'Keg.model'
        db.alter_column(u'beers_keg', 'model', self.gf('django.db.models.fields.CharField')(default=' ', max_length=250))

        # Changing field 'Keg.make'
        db.alter_column(u'beers_keg', 'make', self.gf('django.db.models.fields.CharField')(default=' ', max_length=250))

        # Changing field 'Keg.stampedLoc'
        db.alter_column(u'beers_keg', 'stampedLoc', self.gf('django.db.models.fields.CharField')(default=' ', max_length=250))

        # Changing field 'Keg.stampedOwner'
        db.alter_column(u'beers_keg', 'stampedOwner', self.gf('django.db.models.fields.CharField')(default=' ', max_length=250))

        # Changing field 'Keg.notes'
        db.alter_column(u'beers_keg', 'notes', self.gf('django.db.models.fields.CharField')(default=' ', max_length=250))

        # Changing field 'Keg.serial'
        db.alter_column(u'beers_keg', 'serial', self.gf('django.db.models.fields.CharField')(default=' ', max_length=250))

    models = {
        u'beers.beer': {
            'Meta': {'object_name': 'Beer'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'createdDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fgEst': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'ibuEst': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiedDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ogEst': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('createdDate',)", 'max_length': '50', 'populate_from': "'name'"}),
            'srmEst': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.BeerStyle']"})
        },
        u'beers.beerstyle': {
            'Meta': {'object_name': 'BeerStyle'},
            'abvMax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'abvMin': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'catNum': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'createdDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fgMax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'fgMin': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'ibuMax': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ibuMin': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiedDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'ogMax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'ogMin': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
            'srmMax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'srmMin': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'})
        },
        u'beers.keg': {
            'Meta': {'object_name': 'Keg'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'createdDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kegstatus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.KegStatus']"}),
            'kegtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beers.KegType']"}),
            'label': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modifiedDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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