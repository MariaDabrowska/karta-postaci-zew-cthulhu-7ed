from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kostka.models import Kostka


class WidokIndex(LoginRequiredMixin, generic.TemplateView):
    template_name = 'kostka/index.html'


class WidokKostka(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render(
            request,
            template_name='kostka/kostki.html',
            context={'kostki': Kostka.objects.all()}
        )


class WidokKostkaTworzenie(LoginRequiredMixin, generic.CreateView):
    model = Kostka
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('kostka:kostka-widok')


class WidokKostkaSzczegoly(LoginRequiredMixin, generic.DetailView):
    model = Kostka
    template_name = 'kostka/moja_kostka.html'


class WidokKostkaUaktualnij(LoginRequiredMixin, generic.UpdateView):
    model = Kostka
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('kostka:kostka-widok')


class WidokKostkaUsun(LoginRequiredMixin, generic.DeleteView):
    model = Kostka
    template_name = 'delete.html'
    success_url = reverse_lazy('kostka:kostka-widok')

