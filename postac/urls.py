from django.urls import path

from postac import views

app_name = 'postac'
urlpatterns = [
    path('index/', views.WidokIndex.as_view(), name='index'),

    path('postac-widok/', views.WidokPostac.as_view(), name='postac-widok'),
    path('postacie/', views.WidokPostacLista.as_view(), name='postacie'),
    path('postac-stworz/', views.WidokStworzPostac.as_view(), name='postac-stworz'),
    path('postac-szczegoly/<pk>', views.WidokPostacSzczegoly.as_view(), name='postac-szczegoly'),
    path('postac-uaktualnij/<pk>', views.WidokPostacUaktualnij.as_view(), name='postac-uaktualnij'),
    path('postac-usun/<pk>', views.WidokPostacUsun.as_view(), name='postac-usun'),

    path('generuj-cechy/', views.WidokStworzCechy.as_view(), name='generuj-cechy'),
    path('zastosuj-wiek/', views.ZastosujWiek.as_view(), name='zastosuj_wiek'),
]
