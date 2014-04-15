from django.db import models
from beers.models import Beer
from kegs.models import Keg


class TapManager(models.Manager):
    """Add an additional column with the srm RGB string
        and also sort by tap #
        """
    def get_queryset(self):
        return super(TapManager, self).get_queryset().order_by('number')\
            .extra(select={'srmrgb': 'SELECT rgb from beers_srmrgb WHERE taps_tap.srm_actual = beers_srmrgb.srm'},
                order_by=['number'])


class Tap(models.Model):
    CO2 = 'CO2'
    NITROGEN = 'NITROGEN'
    CASK = 'CASK'
    TAP_TYPE_CODES = (
            (CO2, u"CO\u2082"),
            (NITROGEN, "Nitrogen"),
            (CASK, "Cask"),
    )

    beer = models.ForeignKey(Beer, null=True)
    keg = models.ForeignKey(Keg, null=True)
    number = models.IntegerField(unique=True)
    tap_type =  models.CharField(max_length=20, choices=TAP_TYPE_CODES,
                                                default=CO2)
    active = models.BooleanField(default=True)
    og_actual = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fg_actual = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    srm_actual = models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    ibu_actual =  models.IntegerField(default=0)

    objects = TapManager()

    @property
    def calories(self):
        # You have to cast Decimals to float or the calculations fail
        og = float(self.og_actual)
        fg = float(self.og_actual)

        print "starting calories"
        if (self.og_actual == 1 and self.fg_actual == 1):
            print "0 kCal" 
            return 0
        else:
            print "calculating calories from carbs"
            calories_from_carbs = round(3550 * fg * ((0.1808 * og) + (0.8192 * fg) - 1.0004))
            print "calculating calories from alchol"
            calories_from_alcohol = round(1881.22 * (fg * (og - fg)))
            print "%d kCal" % (calories_from_alcohol + calories_from_carbs)
            return calories_from_alcohol + calories_from_carbs

    @property
    def bugu(self):
    #BU:GU is (ibu/((og-1)*1000)) if og > 1
        if self.og_actual > 1:
            print "bugu"
            return (self.ibu_actual/((self.og_actual-1)*1000)) 
        else:
            return 0

    @property
    def abv(self):
        return (self.og_actual - self.fg_actual) * 131
