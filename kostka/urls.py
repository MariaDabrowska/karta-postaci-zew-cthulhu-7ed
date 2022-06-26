from django.urls import path

from kostka import views

app_name = 'kostka'
urlpatterns = [
    path('index/', views.IndexWidok.as_view(), name='index'),

    path('kostka-widok/', views.KostkaWidok.as_view(), name='kostka-widok'),
    path('kostka-lista-widok/', views.KostkaWidok.as_view(), name='kostka-lista-widok'),
    path('kostka-tworzenie/', views.KostkaTworzenieWidok.as_view(), name='kostka-tworzenie'),
    path('kostka-szczegoly/<pk>', views.KostkaSzczegolowyWidok.as_view(), name='kostka-szczegoly'),
    path('kostka-uaktualnij/<pk>', views.KostkaUaktualnijWidok.as_view(), name='kostka-uaktualnij'),
    path('kostka-usun/<pk>', views.KostkaUsunWidok.as_view(), name='kostka-usun'),

]
