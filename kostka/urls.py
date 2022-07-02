from django.urls import path

from kostka import views

app_name = 'kostka'
urlpatterns = [
    path('index/', views.WidokIndex.as_view(), name='index'),

    path('kostka-widok/', views.WidokKostka.as_view(), name='kostka-widok'),
    path('kostka-lista-widok/', views.WidokKostka.as_view(), name='kostka-lista-widok'),
    path('kostka-tworzenie/', views.WidokKostkaTworzenie.as_view(), name='kostka-tworzenie'),
    path('kostka-szczegoly/<pk>', views.WidokKostkaSzczegoly.as_view(), name='kostka-szczegoly'),
    path('kostka-uaktualnij/<pk>', views.WidokKostkaUaktualnij.as_view(), name='kostka-uaktualnij'),
    path('kostka-usun/<pk>', views.WidokKostkaUsun.as_view(), name='kostka-usun'),

]
