from django.contrib import admin

from postac.models import ZestawCechPostaci, Umiejetnosc, Profesja, Postac


class PostacAdmin(admin.ModelAdmin):
    ordering = ('nazwa',)
    list_display = ('nazwa', 'uzytkownik')
    list_display_links = ('nazwa',)
    list_per_page = 50
    list_filter = ('nazwa', 'uzytkownik')
    search_fields = ('question_text',)
    actions = ('cleanup_text', 'example_suffix')
    fieldsets = [
        ('General', {
            'fields': ['nazwa'],
            'description': 'General_info'
        }),
        ('External Information', {
            'fields': ['uzytkownik', 'wiek', 'cechy', 'um', 'profesja', 'ekwipunek', 'historia', 'uzbrojenie'],
            'description': 'Additional Info'
        })
    ]


class ProfesjaAdmin(admin.ModelAdmin):
    ordering = ('nazwa',)
    list_display = ('nazwa',)
    list_display_links = ('nazwa',)
    list_per_page = 50
    list_filter = ('nazwa',)
    search_fields = ('nazwa',)
    actions = ('cleanup_text', 'example_suffix')
    fieldsets = [
        ('General', {
            'fields': ['nazwa'],
            'description': 'General_info'
        }),
        ('External Information', {
            'fields': ['punkty_do_wydania', 'majetnosc_min', 'majetnosc_max',
                       'um_stale', 'wybor1', 'wybor2', 'wybor3', 'wybor4'],
            'description': 'Additional Info'
        })
    ]


admin.site.register(ZestawCechPostaci)
admin.site.register(Umiejetnosc)
admin.site.register(Profesja, ProfesjaAdmin)
admin.site.register(Postac, PostacAdmin)
