# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'KegStatus'
        db.delete_table(u'kegs_kegstatus')


        # Renaming column for 'Keg.kegstatus' to match new field type.
        db.rename_column(u'kegs_keg', 'kegstatus_id', 'kegstatus')
        # Changing field 'Keg.kegstatus'
        db.alter_column(u'kegs_keg', 'kegstatus', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Removing index on 'Keg', fields ['kegstatus']
        db.delete_index(u'kegs_keg', ['kegstatus_id'])


    def backwards(self, orm):
        # Adding index on 'Keg', fields ['kegstatus']
        db.create_index(u'kegs_keg', ['kegstatus_id'])

        # Adding model 'KegStatus'
        db.create_table(u'kegs_kegstatus', (
            ('code', self.gf('django.db.models.fields.CharField')(default='NEEDS_CLEANING', max_length=20)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'kegs', ['KegStatus'])


        # Renaming column for 'Keg.kegstatus' to match new field type.
        db.rename_column(u'kegs_keg', 'kegstatus', 'kegstatus_id')
        # Changing field 'Keg.kegstatus'
        db.alter_column(u'kegs_keg', 'kegstatus_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kegs.KegStatus']))

    models = {
        u'kegs.keg': {
            'Meta': {'object_name': 'Keg'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kegstatus': ('django.db.models.fields.CharField', [], {'default': "'NEEDS_CLEANING'", 'max_length': '20'}),
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
        u'kegs.kegtype': {
            'Meta': {'object_name': 'KegType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxamount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['kegs']