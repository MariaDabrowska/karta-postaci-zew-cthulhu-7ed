from django.shortcuts import render
from django.views import generic
# Create your views here.
from postac.models import ZestawCechPostaci, Postac
from kostka.models import Kostka

class WidokStworzPostac(generic.CreateView):
    model = Postac
    template_name = ...
    fields = '__all__'
    success_url = #url tworzenia cech

class WidokStworzCechy(generic.CreateView):
    model = ZestawCechPostaci
    template_name = ...

    def post(self, request, *args, **kwargs):
        k6 = Kostka.objects.get(6)
        self.object.sila = k6.rzut()
        ...
        self.object.ruch = self._generuj_ruch()

        return super().post(request, *args, **kwargs)

    def _generuj_ruch(self):
        if self.object.sila > self.object.budowa_ciala and self.object.zrecznosc > self.object.budowa_ciala:
            return 9
        if self.object.sila < self.object.budowa_ciala and self.object.zrecznosc < self.object.budowa_ciala:
            return 7
        return 8

class ZastosujWiek(generic.FormView):
    def form_valid(self, form):
        sila = form.cleaned_data['sila']
        ...
        zestaw_cech = ZestawCechPostaci.objects.get