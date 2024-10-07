from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect

def cadastro_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')  # Se for utilizar email
        senha = request.POST.get('password')  # Use "password" para consistência
    
        user = User.objects.filter(username=username).first()
        if user:
            return render(request, 'authSignin.html', {'error': 'Usuário já existe'})
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect('login')
        

def login_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'loginErro.html', {'error': 'Usuário ou senha inválidos'})
        

def logout_view(request):
    logout(request)
    return redirect('login.html')


@login_required(login_url='/login/')
def home_page(request):
        return render(request, 'home.html')