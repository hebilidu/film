from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render, get_object_or_404
from .models import Country, Category, Director, Film
from .forms import DirectorModelForm, FilmModelForm


# class SuccessMessageMixin:
#     """ Add a success message on successful form submission. """
#     success_message = ''

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         success_message = self.get_success_message(form.cleaned_data)
#         if success_message:
#             messages.success(self.request, success_message)
#         return response

#     def get_success_message(self, cleaned_data):
#         return self.success_message % cleaned_data


class FilmListView(LoginRequiredMixin, generic.ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films' # by default we can use: object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'List Films'
        return context

# def listFilms(request):
#     films = Film.objects.all()
#     return render(request, 'homepage.html', { 'films':films })


class adddirector(LoginRequiredMixin, generic.CreateView):
    model = Director
    fields = '__all__'
    template_name = 'addpage.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Add Director'
        return context    


class  addfilm(LoginRequiredMixin, generic.CreateView):
    model = Film
    fields = '__all__'
    template_name = 'addpage.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Add Film'
        return context 


# login required on def based views
# from django.contrib.auth.decorators import login_required
# @login_required
# def homepage(request):
#     return render().....


class CategoryDetailView(generic.DetailView):
    model = Category
    fields = '__all__'
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'List Categories'
        return context


class DirectorDetailView(generic.DetailView):
    model = Director
    fields = '__all__'
    template_name = 'director.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'View Director Details'
        return context


class DirectorUpdateView(generic.UpdateView):
    model = Director
    fields = '__all__'
    template_name = 'addpage.html'
    success_url = reverse_lazy('homepage')

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Director, id = id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update Director'
        return context 


class DirectorDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Director
    fields = '__all__'
    template_name = 'director.html'
    success_url = reverse_lazy('homepage')
    success_message = "Director deleted successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Delete Director'
        return context 


class FilmDetailView(generic.DetailView):
    model = Film
    fields = '__all__'
    template_name = 'film.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Film, id = id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'View Film Details'
        return context


class FilmUpdateView(generic.UpdateView):
    model = Film
    fields = '__all__'
    template_name = 'addpage.html'
    success_url = reverse_lazy('homepage')

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Film, id = id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update Film'
        return context


class FilmDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Film
    fields = '__all__'
    template_name = 'film.html'
    success_url = reverse_lazy('homepage')
    success_message = "Film deleted successfully"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Film, id = id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Delete Film'
        return context 


# def edit_director(request, pk):
#     director = Director.objects.get(id=pk)

#     if request.method == 'GET':
#         return render(request, 'addpage.html',
#             {'form': DirectorModelForm(instance = director), 'action':'edit Director'})

#     if request.method == 'POST':
#         data = request.POST
#         form = DirectorModelForm(data, instance = director)
#         if form.is_valid():
#             form.save()
#         return redirect('homepage')

# def edit_film(request, pk):
#     film = Film.objects.get(id=pk)

#     if request.method == 'GET':
#         return render(request, 'addpage.html',
#             {'form': FilmModelForm(instance = film), 'action':'edit Film'})

#     if request.method == 'POST':
#         data = request.POST
#         form = FilmModelForm(data, instance = film)
#         if form.is_valid():
#             form.save()
#         return redirect('homepage')
