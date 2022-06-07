import io
import fpdf
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout  as auth_logout
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class FilmeList(LoginRequiredMixin, ListView):
    model = models.Filme

class FilmeDetail(LoginRequiredMixin, DetailView): 
    model = models.Filme

class FilmeCreate(LoginRequiredMixin, CreateView): 
    model = models.Filme
    fields = '__all__'
    def form_valid(self, form):
        filme = form.save()
        return redirect('filme_list')

class FilmeUpdate(LoginRequiredMixin, UpdateView): 
    model = models.Filme
    fields = '__all__'
    def form_valid(self, form):
        filme = form.save()
        return redirect('filme_list')

class FilmeDelete(LoginRequiredMixin, DeleteView): 
    model = models.Filme
    success_url = reverse_lazy('filme_list')

class ClienteList(LoginRequiredMixin, ListView):
    model = models.Cliente

class ClienteDetail(LoginRequiredMixin, DetailView): 
    model = models.Cliente

class ClienteCreate(LoginRequiredMixin, CreateView): 
    model = models.Cliente
    fields = '__all__'
    def form_valid(self, form):
        cliente = form.save()
        return redirect('cliente_list')

class ClienteUpdate(LoginRequiredMixin, UpdateView): 
    model = models.Cliente
    fields = '__all__'
    def form_valid(self, form):
        cliente = form.save()
        return redirect('cliente_list')

class ClienteDelete(LoginRequiredMixin, DeleteView): 
    model = models.Cliente
    success_url = reverse_lazy('cliente_list')

class DiretorList(LoginRequiredMixin, ListView):
    model = models.Diretor

class DiretorDetail(LoginRequiredMixin, DetailView): 
    model = models.Diretor

class DiretorCreate(LoginRequiredMixin, CreateView): 
    model = models.Diretor
    fields = '__all__'
    def form_valid(self, form):
        diretor = form.save()
        return redirect('diretor_list')

class DiretorUpdate(LoginRequiredMixin, UpdateView): 
    model = models.Diretor
    fields = '__all__'
    def form_valid(self, form):
        diretor = form.save()
        return redirect('diretor_list')

class DiretorDelete(LoginRequiredMixin, DeleteView): 
    model = models.Diretor
    success_url = reverse_lazy('diretor_list')

class RoteiristaList(LoginRequiredMixin, ListView):
    model = models.Roteirista

class RoteiristaDetail(LoginRequiredMixin, DetailView): 
    model = models.Roteirista

class RoteiristaCreate(LoginRequiredMixin, CreateView): 
    model = models.Roteirista
    fields = '__all__'
    def form_valid(self, form):
        roteirista = form.save()
        return redirect('roteirista_list')

class RoteiristaUpdate(LoginRequiredMixin, UpdateView): 
    model = models.Roteirista
    fields = '__all__'
    def form_valid(self, form):
        roteirista = form.save()
        return redirect('roteirista_list')

class RoteiristaDelete(LoginRequiredMixin, DeleteView): 
    model = models.Roteirista
    success_url = reverse_lazy('roteirista_list')

class GeneroList(LoginRequiredMixin, ListView):
    model = models.Genero

class GeneroDetail(LoginRequiredMixin, DetailView): 
    model = models.Genero

class GeneroCreate(LoginRequiredMixin, CreateView): 
    model = models.Genero
    fields = '__all__'
    def form_valid(self, form):
        genero = form.save()
        return redirect('genero_list')

class GeneroUpdate(LoginRequiredMixin, UpdateView): 
    model = models.Genero
    fields = '__all__'
    def form_valid(self, form):
        genero = form.save()
        return redirect('genero_list')

class GeneroDelete(LoginRequiredMixin, DeleteView): 
    model = models.Genero
    success_url = reverse_lazy('genero_list')

class AluguelList(LoginRequiredMixin, ListView):
    model = models.Aluguel

class AluguelDetail(LoginRequiredMixin, DetailView): 
    model = models.Aluguel

class AluguelCreate(LoginRequiredMixin, CreateView): 
    model = models.Aluguel
    fields = ('filme', 'cliente', 'prazo_devolucao')

    def form_valid(self, form):
        user = self.request.user
        filme = form.save(commit=False)
        filme.funcionario = user
        filme.save()
        return redirect('aluguel_list')

class AluguelUpdate(LoginRequiredMixin, UpdateView): 
    model = models.Aluguel
    fields = '__all__'
    def form_valid(self, form):
        filme = form.save()
        return redirect('aluguel_list')

class AluguelDelete(LoginRequiredMixin, DeleteView): 
    model = models.Aluguel
    success_url = reverse_lazy('aluguel_list')

class FuncionarioList(LoginRequiredMixin, ListView):
    model = models.Funcionario
    template_name = 'core/funcionario_list.html'
    fields = ('id', 'first_name', 'last_name')

class FuncionarioDetail(LoginRequiredMixin, DetailView): 
    model = models.Funcionario
    fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active')
    template_name = 'core/funcionario_detail.html'

class FuncionarioCreate(LoginRequiredMixin, CreateView): 
    model = models.Funcionario
    fields = ('username', 'email', 'first_name', 'last_name', 'is_active')
    template_name = 'core/funcionario_form.html'

    def form_valid(self, form):
        super().form_valid(form)
        return redirect('funcionario_list')

class FuncionarioUpdate(LoginRequiredMixin, UpdateView): 
    model = models.Funcionario
    fields = ('username', 'email', 'first_name', 'last_name', 'is_active')
    template_name = 'core/funcionario_form.html'

    def form_valid(self, form):
        super().form_valid(form)
        return redirect('funcionario_list')

class FuncionarioDelete(LoginRequiredMixin, DeleteView): 
    model = models.Funcionario
    success_url = reverse_lazy('funcionario_list')
    template_name = 'core/funcionario_confirm_delete.html'


# @login_required
def export_alugueis(request):
    alugueis = models.Aluguel.objects.select_related('cliente', 'filme', 'funcionario').all()
    print(alugueis)
    pseudo_file = io.StringIO()
    fieldnames = (
        'id', 'cliente', 'funcionario', 'data_de_aluguel',
        'prazo_devolucao', 'filme'
    )
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)
    pdf.set_fill_color(193, 229, 252)
    for idx, field in enumerate(fieldnames):
        ln = 1 if idx == len(fieldnames) - 1 else 0
        pdf.cell(30, 10, field, 1, ln, 'C', True)
    pdf.set_font('Arial', '', 8)
    pdf.set_fill_color(235,236,236)
    fill = False
    for aluguel in alugueis:
        serialized_aluguel = {
            'id': str(aluguel.id),
            'cliente': aluguel.cliente.nome,
            'funcionario': aluguel.funcionario.first_name,
            'data_de_aluguel': aluguel.datetime_aluguel.strftime("%d/%m/%Y"),
            'prazo_devolucao': aluguel.prazo_devolucao.strftime("%d/%m/%Y"),
            'filme': aluguel.filme.titulo,
        }
        for idx, field in enumerate(fieldnames):
            ln = 1 if idx == len(fieldnames) - 1 else 0
            pdf.cell(30, 10, serialized_aluguel[field], 1, ln, 'C', fill)
        fill = True
    pdf.output('/tmp/export.pdf', dest='F')
    return FileResponse(open('/tmp/export.pdf', 'rb'), content_type='application/pdf')
