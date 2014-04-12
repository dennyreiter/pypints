from django.db import models

from core.models import Timestampable, Permalinkable


class Glassware(models.Model):
    name = models.CharField(max_length=250)
    notes = models.TextField(blank=True, null=True)
    glass_image =  models.ImageField(upload_to='files/%Y/%m/%d', 
                                        blank=True, null=True)


class NumberBeerManager(models.Manager):
    """Try and sort by the Style number
    FIXME: style category letters are backwards?
    """
    def get_queryset(self):
        return super(NumberBeerManager, self).get_queryset().order_by('category_number','subcategory')


class BeerStyle(models.Model):
    common_name = models.CharField(max_length=250)
    category_number = models.IntegerField()
    subcategory = models.CharField(max_length=1)
    category_name = models.CharField(max_length=250)
    glassware = models.ForeignKey(Glassware, default=1)
    og_min =  models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    og_max =  models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fg_min =  models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fg_max =  models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    abv_min =  models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    abv_max =  models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    ibu_min =  models.IntegerField(default=0)
    ibu_max =  models.IntegerField(default=0)
    srm_min =  models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    srm_max =  models.DecimalField(max_digits=3,
                decimal_places=1, default=0)

    objects = NumberBeerManager()

    class Meta:
        unique_together = ('category_number', 'subcategory',)
        index_together = [
                    ["category_number", "subcategory"],
                    ]

    def __unicode__(self):
        return u"%s -- %s%s(%s)" % (self.common_name, self.category_number,
                                    self.subcategory, self.category_name)


class BeerManager(models.Manager):
    """Add an additional column with the srm RGB string"""
    def get_queryset(self):
        return super(BeerManager, self).get_queryset()\
            .extra(select={'srmrgb': 'SELECT rgb from beers_srmrgb WHERE beers_beer.srm_estimated = beers_srmrgb.srm'},
                order_by=['name'])


class Beer(Permalinkable, Timestampable, models.Model):
    name = models.CharField(db_index=True, max_length=250)
    style = models.ForeignKey(BeerStyle)
    notes = models.TextField(blank=True,null=True)
    og_estimated = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fg_estimated = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    srm_estimated = models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    ibu_estimated =  models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    objects = BeerManager()

    def __unicode__(self):
        return self.name


class SrmRgb(models.Model):
    srm  = models.DecimalField(db_index=True, max_digits=3,
                decimal_places=1, default=0, unique=True)
    rgb = models.CharField(max_length=13)

    def __unicode__(self):
        return self.srm



