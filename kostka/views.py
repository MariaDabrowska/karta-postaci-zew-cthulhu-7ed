from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kostka.models import Kostka


class WidokIndex(generic.TemplateView):
    template_name = 'kostka/index.html'


class WidokKostka(generic.View):
    def get(self, request):
        return render(
            request,
            template_name='kostka/kostki.html',
            context={'kostki': Kostka.objects.all()}
        )


class WidokKostkaLista(generic.ListView):
    template_name = 'kostka/list_view.html'
    model = Kostka


class WidokKostkaTworzenie(generic.CreateView):
    model = Kostka
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('kostka:kostka-widok')


class WidokKostkaSzczegoly(generic.DetailView):
    model = Kostka
    template_name = 'kostka/moja_kostka.html'


class WidokKostkaUaktualnij(generic.UpdateView):
    model = Kostka
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('kostka:kostka-widok')


class WidokKostkaUsun(generic.DeleteView):
    model = Kostka
    template_name = 'delete.html'
    success_url = reverse_lazy('kostka:kostka-widok')

