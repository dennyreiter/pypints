from django.db import models

from core.models import Timestampable


class KegType(models.Model):
    name = models.CharField(max_length=250)
    maxamount = models.DecimalField(max_digits=6,
                decimal_places=2, default=0)

    def __unicode__(self):
        return self.name


class Keg(Timestampable, models.Model):
    SERVING = 'SERVING'
    PRIMARY = 'PRIMARY'
    SECONDARY = 'SECONDARY'
    TERTIARY = 'TERTIARY'
    DRY_HOPPING = 'DRY_HOPPING'
    CONDITIONING = 'CONDITIONING'
    CLEAN = 'CLEAN'
    NEEDS_CLEANING = 'NEEDS_CLEANING'
    NEEDS_PARTS = 'NEEDS_PARTS'
    NEEDS_REPAIRS = 'NEEDS_REPAIRS'
    KEG_STATUS_CODES = (
        (SERVING, 'Serving'),
        (PRIMARY, 'Primary'),
        (SECONDARY, 'Secondary'),
        (TERTIARY, 'Tertiary'),
        (DRY_HOPPING, 'Dry Hopping'),
        (CONDITIONING, 'Conditioning'),
        (CLEAN, 'Clean'),
        (NEEDS_CLEANING, 'Needs Cleaning'),
        (NEEDS_PARTS, 'Needs Parts'),
        (NEEDS_REPAIRS, 'Needs Repairs'),
    )
    label = models.IntegerField(default=0)
    kegtype = models.ForeignKey(KegType)
    make = models.CharField(max_length=250,blank=True,null=True)
    model = models.CharField(max_length=250,blank=True,null=True)
    serial = models.CharField(max_length=250,blank=True,null=True)
    stampedOwner = models.CharField(max_length=250,blank=True,null=True)
    stampedLocation = models.CharField(max_length=250,blank=True,null=True)
    notes = models.CharField(max_length=250,blank=True,null=True)
    kegstatus = models.CharField(max_length=20, choices=KEG_STATUS_CODES,
                                    default=NEEDS_CLEANING)
    weight = models.DecimalField(max_digits=11,
                decimal_places=4, default=0)
    active = models.BooleanField(default=False)


    def __unicode__(self):
        return u"%s -- %s" % (self.label, self.kegtype)

