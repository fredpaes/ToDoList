from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def log_in(request):
    error_messages = []
    if request.user.is_anonymous:
        if request.method == 'POST':
            usuario = request.POST.get('user_name', '')
            passwrd = request.POST.get('user_pwd')

            user = authenticate(username=usuario, password=passwrd)
            if user is None:
                error_messages.append('No hay usuario.')
            elif user.is_active:
                login(request, user)
                return redirect('home')
            else:
                error_messages.append('No está activo')

        context = {'msgs': error_messages}
        return render(request, 'login.html', context)
    else:
        # redirect a la vista lista
        return redirect('home')

@login_required
def log_out(request):
    logout(request)
    return redirect('login')