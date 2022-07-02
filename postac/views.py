from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from postac.forms import FormPostac
from postac.models import ZestawCechPostaci, Postac
from kostka.models import Kostka


class WidokIndex(generic.TemplateView):
    template_name = 'postac/index.html'


class WidokPostac(generic.View):
    def get(self, request):
        return render(
            request,
            template_name='postac/postacie.html',
            context={'postacie': Postac.objects.all()}
        )


class WidokPostacLista(generic.ListView):
    template_name = 'postac/list_view_postacie.html'
    model = Postac


class WidokStworzPostac(generic.FormView):
    form_class = FormPostac
    # template_name = 'postac/create.html'
    template_name = 'form.html'
    success_url = reverse_lazy('postac:postac-widok')

    @login_required
    def dopisz_do_uzytkownika(self, request):
        if request.method == 'POST':
            form = FormPostac(request.POST)
            if form.is_valid():
                uzytkownik = self.request.user.username
                Postac.objects.create(uzytkownik=uzytkownik)

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class WidokPostacSzczegoly(generic.DetailView):
    model = Postac
    template_name = 'postac/postac.html'


class WidokPostacUaktualnij(generic.UpdateView):
    model = Postac
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('postac:postac-widok')


class WidokPostacUsun(generic.DeleteView):
    model = Postac
    template_name = 'postac/delete-postac.html'
    success_url = reverse_lazy('postac:postac-widok')


class WidokStworzCechy(generic.CreateView):
    model = ZestawCechPostaci
    template_name = ...

    def post(self, request, args, **kwargs):
        k6 = Kostka.objects.get(6)

        self.object.sila = k6.rzuty_modyfikowane1()
        self.object.kondycja = k6.rzuty_modyfikowane1()
        self.object.budowa_ciala = k6.rzuty_modyfikowane2()
        self.object.zrecznosc = k6.rzuty_modyfikowane1()
        self.object.wyglad = k6.rzuty_modyfikowane1()
        self.object.inteligencja = k6.rzuty_modyfikowane2()
        self.object.moc = k6.rzuty_modyfikowane1()
        self.object.wyksztalcenie = k6.rzuty_modyfikowane2()
        self.object.szczescie = k6.rzuty_modyfikowane1()
        self.object.krzepa = self._generuj_krzepa()
        self.object.mod_obr = self._generuj_mod_ob()
        self.object.wytrzymalosc = self._generuj_wytrzymalosc()
        self.object.ruch = self._generuj_ruch()

        return super().post(request, args, **kwargs)

    def _generuj_krzepa(self):
        if self.object.sila + self.object.budowa_ciala < 65:
            return -2
        if self.object.sila + self.object.budowa_ciala < 85:
            return -1
        if self.object.sila + self.object.budowa_ciala < 125:
            return 0
        if self.object.sila + self.object.budowa_ciala < 165:
            return 1
        if self.object.sila + self.object.budowa_ciala < 205:
            return 2

    def _generuj_mod_ob(self):
        if self.object.krzepa == 1:
            return '+1k4'
        if self.object.krzepa == 2:
            return '+1k6'
        return self.object.krzepa

    def _generuj_wytrzymalosc(self):
        return (self.object.kondycja + self.object.budowa_ciala) // 10

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
