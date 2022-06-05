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


class CatalogoList(ListView):
    model = models.Filme

class CatalogoDetail(DetailView): 
	model = models.Filme

class CadastroList(ListView):
    model = models.Cliente

class CadastroDetail(DetailView): 
	model = models.Cliente