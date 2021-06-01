from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'registration/signup.html', { 'form': UserCreationForm() })

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/signup.html', { 'form':form })


class ProfileView(generic.CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profile.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'add'
        return context 
