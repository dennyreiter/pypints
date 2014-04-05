# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BeerStyle'
        db.create_table(u'beers_beerstyle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('catNum', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ogMin', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('ogMax', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('fgMin', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('fgMax', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('abvMin', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('abvMax', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('ibuMin', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ibuMax', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('srmMin', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('srmMax', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('createdDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modifiedDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'beers', ['BeerStyle'])

        # Adding model 'Beer'
        db.create_table(u'beers_beer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beers.BeerStyle'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('ogEst', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('fgEst', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('srmEst', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('ibuEst', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('createdDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modifiedDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'beers', ['Beer'])

        # Adding model 'SrmRgb'
        db.create_table(u'beers_srmrgb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('srm', self.gf('django.db.models.fields.DecimalField')(default=0, unique=True, max_digits=3, decimal_places=1)),
            ('rgb', self.gf('django.db.models.fields.CharField')(max_length=13)),
        ))
        db.send_create_signal(u'beers', ['SrmRgb'])

        # Adding model 'KegType'
        db.create_table(u'beers_kegtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('maxamount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'beers', ['KegType'])

        # Adding model 'KegStatus'
        db.create_table(u'beers_kegstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'beers', ['KegStatus'])

        # Adding model 'Keg'
        db.create_table(u'beers_keg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kegtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beers.KegType'])),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('stampedOwner', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('stampedLoc', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('kegstatus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beers.KegStatus'])),
            ('weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=11, decimal_places=4)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('createdDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modifiedDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'beers', ['Keg'])

        # Adding model 'Tap'
        db.create_table(u'beers_tap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beers.Beer'])),
            ('keg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beers.Keg'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ogAct', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('fgAct', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=3)),
            ('srmAct', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1)),
            ('ibuAct', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'beers', ['Tap'])


    def backwards(self, orm):
        # Deleting model 'BeerStyle'
        db.delete_table(u'beers_beerstyle')

        # Deleting model 'Beer'
        db.delete_table(u'beers_beer')

        # Deleting model 'SrmRgb'
        db.delete_table(u'beers_srmrgb')

        # Deleting model 'KegType'
        db.delete_table(u'beers_kegtype')

        # Deleting model 'KegStatus'
        db.delete_table(u'beers_kegstatus')

        # Deleting model 'Keg'
        db.delete_table(u'beers_keg')

        # Deleting model 'Tap'
        db.delete_table(u'beers_tap')


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
            'notes': ('django.db.models.fields.TextField', [], {}),
            'ogEst': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '3'}),
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
            'make': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'modifiedDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'stampedLoc': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'stampedOwner': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
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