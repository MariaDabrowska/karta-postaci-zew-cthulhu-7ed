from django.urls import path

from postac import views

app_name = 'postac'
urlpatterns = [
    path('index/', views.WidokIndex.as_view(), name='index'),

    path('postac-widok/', views.WidokPostac.as_view(), name='postac-widok'),
    path('postac-stworz/', views.WidokStworzPostac.as_view(), name='postac-stworz'),
    path('postac-szczegoly/<pk>', views.WidokPostacSzczegoly.as_view(), name='postac-szczegoly'),
    path('postac-uaktualnij/<pk>', views.WidokPostacUaktualnij.as_view(), name='postac-uaktualnij'),
    path('postac-usun/<pk>', views.WidokPostacUsun.as_view(), name='postac-usun'),

    path('zestaw-cech-widok/', views.WidokCecha.as_view(), name='zestaw-cech-widok'),
    path('zestaw-cech-stworz/', views.WidokStworzCechy.as_view(), name='zestaw-cech-stworz'),
    path('zestaw-cech-szczegoly/<pk>', views.WidokCechaSzczegoly.as_view(), name='zestaw-cech-szczegoly'),
    path('zestaw-cech-uaktualnij/<pk>', views.WidokCechaUaktualnij.as_view(), name='zestaw-cech-uaktualnij'),
    path('zestaw-cech-usun/<pk>', views.WidokCechaUsun.as_view(), name='zestaw-cech-usun'),

    path('profesja-widok/', views.WidokProfesja.as_view(), name='profesja-widok'),
    path('profesja-stworz/', views.WidokStworzProfesja.as_view(), name='profesja-stworz'),
    path('profesja-szczegoly/<pk>', views.WidokProfesjaSzczegoly.as_view(), name='profesja-szczegoly'),
    path('profesja-uaktualnij/<pk>', views.WidokProfesjaUaktualnij.as_view(), name='profesja-uaktualnij'),
    path('profesja-usun/<pk>', views.WidokProfesjaUsun.as_view(), name='profesja-usun'),

    path('zastosuj-wiek/', views.ZastosujWiek.as_view(), name='zastosuj_wiek'),
]
