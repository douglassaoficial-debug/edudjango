# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import * # * = Tudo
from .forms import CursoForm, AvaliacaoForm

def home_view(request):
    avaliacoes = Avaliacao.objects.all()

    context = {
        'avaliacoes' : avaliacoes,
        'nome_empresa': 'EduDjango',
    }

    return render(request, 'home.html', context)

def perfil_view(request):
    context = {
        'nome_funcionario': request.user.username,
        'cargo': 'Gerente',
        'setor': 'TI',
    }

    return render(request, 'perfil.html', context)

def status_view(request):
    context = {
        'id_servidor': "Servidor Alpha-01",
        'status_sistema': "Operacional",
    }

    return render(request, 'status.html', context)

def cursos_view(request):
    # 1. O usuário clicou no botão "Salvar" do Modal? (POST)
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save() # Salva no banco!
            # Redireciona para a mesma página para "limpar" o formulário e mostrar o novo curso na lista
            return redirect('cursos') 
            
    # 2. O usuário apenas acessou a página normalmente? (GET)
    else:
        form = CursoForm() # Cria um formulário vazio para ficar guardado no Modal

    # Se o usuário enviou o formulário do Modal (POST)
    if request.method == 'POST':
        form_avaliacao = AvaliacaoForm(request.POST)
        if form_avaliacao.is_valid():
            form_avaliacao.save()
            # Redireciona para recarregar a página e limpar o form
            return redirect('cursos') 
    else:
        # Se ele só acessou a página (GET), cria um form vazio
        form_avaliacao = AvaliacaoForm()

    # Busca todos os cursos para exibir na lista
    cursos = Curso.objects.all()

    #OPCIONAL, Só se quiser que apareça a lista de avaliações na tela
    # avaliacoes = Avaliacao.objects.all()

    context = {
        'cursos': cursos,
        'form': form, #  Manda o formulário pro HTML / Não esqueça de passar para o contexto
        'form_avaliacao': form_avaliacao,
        'usuario': request.user.username,
        #'avaliacao' : avaliacoes, #OPCIONAL
    }

    return render(request, 'cursos.html', context)

    # Essa view agora só aceita requisições POST (quando o botão Salvar é clicado)
            
def login_view(request):
    # Começa com a mensagem vazia
    message = None

    if request.method == 'POST':
        # Passamos o request e os dados digitados
        form = AuthenticationForm(request, data=request.POST)
        
        # Se o usuário e senha estiverem corretos no banco
        if form.is_valid():
            user = form.get_user() # Resgata o usuário do banco
            login(request, user)   # Cria a sessão (Faz o login de fato)
            return redirect('home') # Manda para a página inicial
        
        else:
            message = 'Usuário ou senha incorretos! Tente novamente.'

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'message': message,
    }

    return render(request, 'login.html', context)

def cadastro_view(request):
    # Se o usuário clicou no botão de enviar (POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        # Verifica se as senhas batem e se o usuário já não existe
        if form.is_valid():
            form.save() # AGORA SIM ESTÁ SALVANDO NO BANCO!
            return redirect('login') # Redireciona para a tela de login
            
    # Se o usuário apenas acessou a página pela URL (GET)
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'cadastro.html', context)

def logout_view(request):
    logout(request)

    return redirect('login')

