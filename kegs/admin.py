from django.contrib import admin

# Register your models here.
from kegs.models import KegType
from kegs.models import Keg

admin.site.register(KegType)
admin.site.register(Keg)

