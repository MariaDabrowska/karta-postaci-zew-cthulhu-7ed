from django.urls import path
from postac.views import WidokStworzPostac, WidokStworzCechy, ZastosujWiek

app_name = 'postac'
urlpatterns = [
    path('stworz-postac/', WidokStworzPostac.as_view(), name='stworz_postac'),
    path('generuj-cechy/', WidokStworzCechy.as_view(), name='generuj_cechy'),
    path('zastosuj-wiek/', ZastosujWiek.as_view(), name='zastosuj_wiek'),
]
