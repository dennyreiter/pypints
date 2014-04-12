from django.db import models

from core.models import Timestampable


class KegType(models.Model):
    name = models.CharField(max_length=250)
    maxamount = models.DecimalField(max_digits=6,
                decimal_places=2, default=0)

    def __unicode__(self):
        return self.name


class KegStatus(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Keg Statuses"


class Keg(Timestampable, models.Model):
    label = models.IntegerField(default=0)
    kegtype = models.ForeignKey(KegType)
    make = models.CharField(max_length=250,blank=True,null=True)
    model = models.CharField(max_length=250,blank=True,null=True)
    serial = models.CharField(max_length=250,blank=True,null=True)
    stampedOwner = models.CharField(max_length=250,blank=True,null=True)
    stampedLocation = models.CharField(max_length=250,blank=True,null=True)
    notes = models.CharField(max_length=250,blank=True,null=True)
    kegstatus = models.ForeignKey(KegStatus)
    weight = models.DecimalField(max_digits=11,
                decimal_places=4, default=0)
    active = models.BooleanField(default=False)


    def __unicode__(self):
        return u"%s -- %s" % (self.label, self.kegtype)

