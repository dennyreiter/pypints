# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KegType'
        db.create_table(u'kegs_kegtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('maxamount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'kegs', ['KegType'])

        # Adding model 'KegStatus'
        db.create_table(u'kegs_kegstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'kegs', ['KegStatus'])

        # Adding model 'Keg'
        db.create_table(u'kegs_keg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('label', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kegtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kegs.KegType'])),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('stampedOwner', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('stampedLocation', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('kegstatus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kegs.KegStatus'])),
            ('weight', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=11, decimal_places=4)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'kegs', ['Keg'])


    def backwards(self, orm):
        # Deleting model 'KegType'
        db.delete_table(u'kegs_kegtype')

        # Deleting model 'KegStatus'
        db.delete_table(u'kegs_kegstatus')

        # Deleting model 'Keg'
        db.delete_table(u'kegs_keg')


    models = {
        u'kegs.keg': {
            'Meta': {'object_name': 'Keg'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kegstatus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kegs.KegStatus']"}),
            'kegtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kegs.KegType']"}),
            'label': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'stampedLocation': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'stampedOwner': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '4'})
        },
        u'kegs.kegstatus': {
            'Meta': {'object_name': 'KegStatus'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'kegs.kegtype': {
            'Meta': {'object_name': 'KegType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxamount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['kegs']