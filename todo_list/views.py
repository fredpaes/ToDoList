from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import List
from .forms import ListForm

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

@login_required
def supr(request, todo_id):
    item = List.objects.get(pk=todo_id)
    item.delete()
    messages.success(request, ('El item ha sido borrado'))
    return redirect('home')

@login_required
def cross_on(request, todo_id):
    item = List.objects.get(pk=todo_id)
    item.completed = True
    item.save()
    return redirect('home')

@login_required
def uncross(request, todo_id):
    item = List.objects.get(pk=todo_id)
    item.completed = False
    item.save()
    return redirect('home')

@login_required
def edit(request, todo_id):
    item = List.objects.get(pk=todo_id)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('El item ha sido editado'))
            return redirect('home')
    else:
        context = { 'item': item }
        return render(request, 'edit.html', context)
