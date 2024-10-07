from django.shortcuts import render

def atividades_view(request):
    return render(request, 'atividades.html')


def criar_atividade(request):
    return render(request, 'cadastrarAtividades.html')