from django.contrib import admin
from Backend.models import CatDb, MultiDb
from Frontend.models import SubscribeDb

# Register your models here.
admin.site.register(CatDb)
admin.site.register(MultiDb)
admin.site.register(SubscribeDb)
