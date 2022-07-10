from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from postac.forms import FormPostac
from postac.models import ZestawCechPostaci, Postac, Profesja
from kostka.models import Kostka
from postac.utils import GeneratorCech, ZastosujWiek


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
        obj.cechy = ZastosujWiek.zastosuj_wiek(cechy=obj.cechy, wiek=obj.wiek)
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
