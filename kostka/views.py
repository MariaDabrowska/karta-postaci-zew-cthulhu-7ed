from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kostka.models import Kostka


class IndexWidok(generic.TemplateView):
    template_name = 'kostka/index.html'


class KostkaWidok(generic.View):
    def get(self, request):
        return render(
            request,
            template_name='kostka/kostki.html',
            context={'kostki': Kostka.objects.all()}
        )


class KostkaListaWidok(generic.ListView):
    template_name = 'kostka/list_view.html'
    model = Kostka


class KostkaTworzenieWidok(generic.CreateView):
    model = Kostka
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('kostka:kostka-widok')


class KostkaSzczegolowyWidok(generic.DetailView):
    model = Kostka
    template_name = 'kostka/moja_kostka.html'


class KostkaUaktualnijWidok(generic.UpdateView):
    model = Kostka
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('kostka:kostka-widok')


class KostkaUsunWidok(generic.DeleteView):
    model = Kostka
    template_name = 'delete.html'
    success_url = reverse_lazy('kostka:kostka-widok')

