from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from postac.forms import FormPostac
from postac.models import ZestawCechPostaci, Postac, Profesja
from kostka.models import Kostka
from postac.utils import GeneratorCech


class WidokIndex(LoginRequiredMixin, generic.TemplateView):
    template_name = 'postac/index.html'


class WidokCecha(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render(
            request,
            template_name='postac/zestawy_cech.html',
            context={'zestawy_cech': ZestawCechPostaci.objects.all()}
        )


class WidokCechaSzczegoly(LoginRequiredMixin, generic.DetailView):
    model = ZestawCechPostaci
    template_name = 'postac/zestaw_cech.html'


class WidokCechaUaktualnij(LoginRequiredMixin, generic.UpdateView):
    model = ZestawCechPostaci
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('postac:zestaw-cech-widok')


class WidokCechaUsun(LoginRequiredMixin, generic.DeleteView):
    model = ZestawCechPostaci
    template_name = 'delete.html'
    success_url = reverse_lazy('postac:zestaw-cech-widok')


class WidokPostac(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render(
            request,
            template_name='postac/postacie.html',
            context={'postacie': Postac.objects.all()}
        )


class WidokStworzPostac(LoginRequiredMixin, generic.FormView):
    form_class = FormPostac
    template_name = 'postac/form.html'
    success_url = reverse_lazy('postac:postac-widok')
    extra_context = {
    }

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.uzytkownik = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        if not self.request.POST.get('cechy'):
            cechy = GeneratorCech.wygeneruj_cechy()
            form = self.form_class(initial={'cechy': cechy})
        return self.render_to_response(self.get_context_data(form=form))


class WidokPostacSzczegoly(LoginRequiredMixin, generic.DetailView):
    model = Postac
    template_name = 'postac/postac.html'


class WidokPostacUaktualnij(LoginRequiredMixin, generic.UpdateView):
    model = Postac
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('postac:postac-widok')


class WidokPostacUsun(LoginRequiredMixin, generic.DeleteView):
    model = Postac
    template_name = 'postac/delete-postac.html'
    success_url = reverse_lazy('postac:postac-widok')


class ZastosujWiek(LoginRequiredMixin, generic.FormView):  # na tę chwilę to schemat, żeby mieć zapisane zależności
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


class WidokProfesja(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render(
            request,
            template_name='postac/profesje.html',
            context={'profesje': Profesja.objects.all()}
        )


class WidokStworzProfesja(LoginRequiredMixin, generic.CreateView):
    model = Profesja
    fields = '__all__'
    template_name = 'postac/list_view_profesje.html'
    success_url = reverse_lazy('postac:profesja-widok')


class WidokProfesjaSzczegoly(LoginRequiredMixin, generic.DetailView):
    model = Profesja
    template_name = 'postac/profesja.html'


class WidokProfesjaUaktualnij(LoginRequiredMixin, generic.UpdateView):
    model = Profesja
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('postac:profesja-widok')


class WidokProfesjaUsun(LoginRequiredMixin, generic.UpdateView):
    model = Profesja
    template_name = 'form.html'
    success_url = reverse_lazy('postac:profesja-widok')
