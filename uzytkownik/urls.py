from django.urls import path

from uzytkownik import views

app_name = 'uzytkownik'
urlpatterns = [
    path('rejestracja/', views.RejestracjaUzytkownika.as_view(), name='rejestracja')
]
