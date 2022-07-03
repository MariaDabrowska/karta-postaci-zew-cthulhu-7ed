from django.contrib import admin
from kostka.models import Kostka


class KostkaAdimn(admin.ModelAdmin):
    ordering = ('ilosc_scian',)
    list_display = ('ilosc_scian',)
    list_display_links = ('ilosc_scian',)
    list_per_page = 20
    list_filter = ('ilosc_scian',)
    search_fields = ('ilosc scian',)
    actions = ('cleanup_text', 'example_suffix')
    fieldsets = [
        ('General', {
            'fields': ['ilosc_scian'],
            'description': 'General_info'
        })
    ]


admin.site.register(Kostka, KostkaAdimn)
