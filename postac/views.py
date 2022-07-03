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
    fields = '__all__'
    template_name = 'postac/list_view.html'

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
        self.object.poczytalnosc = self.object.moc  # czy to tak zadziała, czy potrzeba GETa?
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


class ZastosujWiek(generic.FormView):  #na tę chwilę to schemat, żeby mieć zapisane zależności
    template_name = "form.html"
    form_class = ...
    success_url = ...  # wybierz profesję

    def test_rozwoju(self, value):
        k100 = Kostka.objects.get(100)
        k10 = Kostka.objects.get(10)
        if k100.rzut() > value:
            return k10.rzut()
        return 0

    def form_valid(self, form):
        result = super().form_valid(form)
        wiek = form.cleaned_data['wiek']
        szczescie = form.cleaned_data['szczescie']
        sila = form.cleaned_data['sila']
        budowa_ciala = form.cleaned_data['budowa_ciala']
        kondycja = form.cleaned_data['kondycja']
        zrecznosc = form.cleaned_data['zrecznosc']
        wyglad = form.cleaned_data['wyglad']
        wyksztalcenie = form.cleaned_data['wyksztalcenie']
        ruch = form.cleaned_data['ruch']
        punkty_do_odjecia = 0
        zestaw_cech = ZestawCechPostaci.objects.get

        if wiek < 20:
            k6 = Kostka.objects.get(6)
            wyksztalcenie -= 5
            szczescie = max(szczescie, k6.rzuty_modyfikowane1)
            punkty_do_odjecia = 5
            sila, budowa_ciala
        elif wiek < 40:
            wyksztalcenie += self.test_rozwoju(wyksztalcenie)
        elif wiek < 50:
            ruch -= 1
            wyglad -= 5
            punkty_do_odjecia = 5
            sila, kondycja, zrecznosc
            for _ in range(2):
                wyksztalcenie += self.test_rozwoju(wyksztalcenie)
        elif wiek < 60:
            ruch -= 2
            wyglad -= 10
            punkty_do_odjecia = 10
            sila, kondycja, zrecznosc
            for _ in range(3):
                wyksztalcenie += self.test_rozwoju(wyksztalcenie)
        elif wiek < 70:
            ruch -= 3
            wyglad -= 15
            punkty_do_odjecia = 20
            sila, kondycja, zrecznosc
            for _ in range(4):
                wyksztalcenie += self.test_rozwoju(wyksztalcenie)
        elif wiek < 80:
            ruch -= 4
            wyglad -= 20
            punkty_do_odjecia = 40
            sila, kondycja, zrecznosc
            for _ in range(4):
                wyksztalcenie += self.test_rozwoju(wyksztalcenie)
        else:
            ruch -= 5
            wyglad -= 25
            punkty_do_odjecia = 80
            sila, kondycja, zrecznosc
            for _ in range(4):
                wyksztalcenie += self.test_rozwoju(wyksztalcenie)



        form.save()
        return result


