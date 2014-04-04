from django.contrib import admin

from beers.models import BeerStyle
from beers.models import Beer
from beers.models import KegType
from beers.models import KegStatus
from beers.models import Keg
from beers.models import Tap

# Register your models here.

admin.site.register(BeerStyle)
admin.site.register(Beer)
admin.site.register(KegType)
admin.site.register(KegStatus)
admin.site.register(Keg)
admin.site.register(Tap)
