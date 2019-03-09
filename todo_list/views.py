from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

@login_required
def add(request):
    msg = ''
    msg_type = ''
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Se agregó con éxito'
            msg_type = True
            form = ListForm()
        else:
            msg_type = False
            msg = 'Ocurrió un problema'
    else:
        form = ListForm()

    context = {
        'form': form,
        'msg': msg,
        'msg_type': msg_type
    }

    return render(request, 'add.html', context)


