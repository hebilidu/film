from django.shortcuts import redirect, render
from django.views import generic
from .models import Country, Category, Director, Film
from django.urls import reverse_lazy


class FilmListView(generic.ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'

# def listFilms(request):
#     films = Film.objects.all()
#     return render(request, 'homepage.html', { 'films':films })


class adddirector(generic.CreateView):
    model = Director
    fields = '__all__'
    template_name = 'addpage.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_type'] = 'Director'
        return context    


class  addfilm(generic.CreateView):
    model = Film
    fields = '__all__'
    template_name = 'addpage.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_type'] = 'Film'
        return context 
