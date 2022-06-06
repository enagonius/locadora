from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout  as auth_logout
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core import models


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html')


def login(request):
    form = AuthenticationForm()
    context = {"form": form}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        context['form'] = form
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                request,
                username=cleaned_data['username'],
                password=cleaned_data['password']
            )
            if user:
                auth_login(request, user)
                return redirect('home')
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('login')


class FilmeList(ListView):
    model = models.Filme

class FilmeDetail(DetailView): 
    model = models.Filme

class FilmeCreate(CreateView): 
    model = models.Filme
    fields = '__all__'
    def form_valid(self, form):
        filme = form.save()
        return redirect('filme_list')

class FilmeUpdate(UpdateView): 
    model = models.Filme
    fields = '__all__'
    def form_valid(self, form):
        filme = form.save()
        return redirect('filme_list')

class FilmeDelete(DeleteView): 
    model = models.Filme
    success_url = reverse_lazy('filme_list')

class ClienteList(ListView):
    model = models.Cliente

class ClienteDetail(DetailView): 
    model = models.Cliente

class ClienteCreate(CreateView): 
    model = models.Cliente
    fields = '__all__'
    def form_valid(self, form):
        cliente = form.save()
        return redirect('cliente_list')

class ClienteUpdate(UpdateView): 
    model = models.Cliente
    fields = '__all__'
    def form_valid(self, form):
        cliente = form.save()
        return redirect('cliente_list')

class ClienteDelete(DeleteView): 
    model = models.Cliente
    success_url = reverse_lazy('cliente_list')

class DiretorList(ListView):
    model = models.Diretor

class DiretorDetail(DetailView): 
    model = models.Diretor

class DiretorCreate(CreateView): 
    model = models.Diretor
    fields = '__all__'
    def form_valid(self, form):
        diretor = form.save()
        return redirect('diretor_list')

class DiretorUpdate(UpdateView): 
    model = models.Diretor
    fields = '__all__'
    def form_valid(self, form):
        diretor = form.save()
        return redirect('diretor_list')

class DiretorDelete(DeleteView): 
    model = models.Diretor
    success_url = reverse_lazy('diretor_list')

class RoteiristaList(ListView):
    model = models.Roteirista

class RoteiristaDetail(DetailView): 
    model = models.Roteirista

class RoteiristaCreate(CreateView): 
    model = models.Roteirista
    fields = '__all__'
    def form_valid(self, form):
        roteirista = form.save()
        return redirect('roteirista_list')

class RoteiristaUpdate(UpdateView): 
    model = models.Roteirista
    fields = '__all__'
    def form_valid(self, form):
        roteirista = form.save()
        return redirect('roteirista_list')

class RoteiristaDelete(DeleteView): 
    model = models.Roteirista
    success_url = reverse_lazy('roteirista_list')

class GeneroList(ListView):
    model = models.Genero

class GeneroDetail(DetailView): 
    model = models.Genero

class GeneroCreate(CreateView): 
    model = models.Genero
    fields = '__all__'
    def form_valid(self, form):
        genero = form.save()
        return redirect('genero_list')

class GeneroUpdate(UpdateView): 
    model = models.Genero
    fields = '__all__'
    def form_valid(self, form):
        genero = form.save()
        return redirect('genero_list')

class GeneroDelete(DeleteView): 
    model = models.Genero
    success_url = reverse_lazy('genero_list')

class AluguelList(ListView):
    model = models.Aluguel

class AluguelDetail(DetailView): 
    model = models.Aluguel

class AluguelCreate(CreateView): 
    model = models.Aluguel
    fields = '__all__'
    def form_valid(self, form):
        filme = form.save()
        return redirect('aluguel_list')

class AluguelUpdate(UpdateView): 
    model = models.Aluguel
    fields = '__all__'
    def form_valid(self, form):
        filme = form.save()
        return redirect('aluguel_list')

class AluguelDelete(DeleteView): 
    model = models.Aluguel
    success_url = reverse_lazy('aluguel_list')