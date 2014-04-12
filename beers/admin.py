from django.contrib import admin

from beers.models import BeerStyle
from beers.models import Beer
from beers.models import Glassware

# Register your models here.

admin.site.register(BeerStyle)
admin.site.register(Beer)
admin.site.register(Glassware)
