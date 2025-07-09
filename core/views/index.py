from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from rolepermissions.roles import assign_role

@login_required
def index(request):
    return render(request, 'core/index.html')

def criar_user_rh(request):
    user = User.objects.create_user(
        username='renan_rh',
        password='RE0101si@')
    user.save()
    assign_role(user, 'rh')
    return HttpResponse("Usuário RH criado com sucesso!")   