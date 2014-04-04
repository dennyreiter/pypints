from django.db import models

# Create your models here.

class BeerStyle(models.Model):
    name = models.CharField(max_length=250)
    catNum = models.CharField(max_length=5)
    category = models.CharField(max_length=250)
    ogMin =  models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    ogMax =  models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fgMin =  models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fgMax =  models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    abvMin =  models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    abvMax =  models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    ibuMin =  models.IntegerField(default=0)
    ibuMax =  models.IntegerField(default=0)
    srmMin =  models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    srmMax =  models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    
class Beer(models.Model):
    name = models.CharField(max_length=250)
    style = models.ForeignKey(BeerStyle)
    notes = models.TextField()
    ogEst = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fgEst = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    srmEst = models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    ibuEst =  models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class SrmRgb(models.Model):
    srm  = models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    rgb = models.CharField(max_length=13)

    def __unicode__(self):
        return self.srm


class KegType(models.Model):
    name = models.CharField(max_length=250)
    maxamount = models.DecimalField(max_digits=6,
                decimal_places=2, default=0)

    def __unicode__(self):
        return self.srm


class KegStatus(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Keg Statuses"


class Keg(models.Model):
    label = models.IntegerField(default=0)
    kegtype = models.ForeignKey(KegType)
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    serial = models.CharField(max_length=250)
    stampedOwner = models.CharField(max_length=250)
    stampedLoc = models.CharField(max_length=250)
    notes = models.CharField(max_length=250)
    kegstatus = models.ForeignKey(KegStatus)
    weight = models.DecimalField(max_digits=11,
                decimal_places=4, default=0)
    active = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return u"%s -- %s" % (self.label, self.kegtype)


class Tap(models.Model):
    beer = models.ForeignKey(Beer)
    keg = models.ForeignKey(Keg)
    number = models.IntegerField()
    active = models.BooleanField(default=False)
    ogAct = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fgAct = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    srmAct = models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    ibuAct =  models.IntegerField(default=0)

