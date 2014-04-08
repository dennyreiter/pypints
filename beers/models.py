from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class CategoryBeerManager(models.Manager):
    def get_queryset(self):
        return super(CategoryBeerManager, self).get_queryset().order_by('category', 'name')


class NumberBeerManager(models.Manager):
    def get_queryset(self):
#        return super(NumberBeerManager, self).get_queryset().order_by('catNum')
# .extra(select={'int_name': 'CAST(t.name AS INTEGER)'},
#                      order_by=['int_name'])
#        return super(NumberBeerManager, self).get_queryset().order_by('catNum')
        return super(NumberBeerManager, self).get_queryset()\
            .extra(select={'int_name': 'CAST(beers_beerstyle.catNum AS INTEGER)'},
                order_by=['int_name','-catNum'])


class NameBeerManager(models.Manager):
    def get_queryset(self):
        return super(NameBeerManager, self).get_queryset().order_by('name')


class BeerStyle(models.Model):
    name = models.CharField(max_length=250)
    catNum = models.CharField(max_length=5, unique=True)
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

    objects = NumberBeerManager()
    object_by_name = NameBeerManager()
    object_by_category = CategoryBeerManager()

    def __unicode__(self):
        return u"%s -- %s(%s)" % (self.name, self.catNum, self.category)

    
class Beer(models.Model):
    name = models.CharField(max_length=250)
    slug =  AutoSlugField(populate_from = 'name',
                        unique_with = 'createdDate')
    style = models.ForeignKey(BeerStyle)
    notes = models.TextField(blank=True,null=True)
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
                decimal_places=1, default=0, unique=True)
    rgb = models.CharField(max_length=13)

    def __unicode__(self):
        return self.srm


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


class Keg(models.Model):
    label = models.IntegerField(default=0)
    kegtype = models.ForeignKey(KegType)
    make = models.CharField(max_length=250,blank=True,null=True)
    model = models.CharField(max_length=250,blank=True,null=True)
    serial = models.CharField(max_length=250,blank=True,null=True)
    stampedOwner = models.CharField(max_length=250,blank=True,null=True)
    stampedLoc = models.CharField(max_length=250,blank=True,null=True)
    notes = models.CharField(max_length=250,blank=True,null=True)
    kegstatus = models.ForeignKey(KegStatus)
    weight = models.DecimalField(max_digits=11,
                decimal_places=4, default=0)
    active = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return u"%s -- %s" % (self.label, self.kegtype)

class TapManager(models.Manager):
    def get_queryset(self):
        return super(TapManager, self).get_queryset().order_by('number')

class Tap(models.Model):
    beer = models.ForeignKey(Beer)
    keg = models.ForeignKey(Keg)
    number = models.IntegerField(unique=True)
    active = models.BooleanField(default=False)
    ogAct = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fgAct = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    srmAct = models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    ibuAct =  models.IntegerField(default=0)

    objects = TapManager()
