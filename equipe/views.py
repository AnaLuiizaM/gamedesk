from django.shortcuts import render

def equipe_view(request):
    return render (request, 'equipe.html')


def cadastro_view(request):
    return render (request, 'cadastrarEquipe.html')