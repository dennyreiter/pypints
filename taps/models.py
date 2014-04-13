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

    beer = models.ForeignKey(Beer)
    keg = models.ForeignKey(Keg)
    number = models.IntegerField(unique=True)
    tap_type =  models.CharField(max_length=20, choices=TAP_TYPE_CODES,
                                                default=CO2)
    active = models.BooleanField(default=False)
    og_actual = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    fg_actual = models.DecimalField(max_digits=4,
                decimal_places=3, default=0)
    srm_actual = models.DecimalField(max_digits=3,
                decimal_places=1, default=0)
    ibu_actual =  models.IntegerField(default=0)

    objects = TapManager()

