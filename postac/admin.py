from django.contrib import admin

from postac.models import ZestawCechPostaci, Umiejetnosc, Profesja, Postac

admin.site.register(ZestawCechPostaci)
admin.site.register(Umiejetnosc)
admin.site.register(Profesja)
admin.site.register(Postac)