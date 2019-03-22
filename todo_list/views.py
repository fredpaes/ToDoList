from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from .models import List
from .forms import ListForm

# Create your views here.
@login_required
def home(request):
    # all_items = List.objects.filter(owner=request.user).order_by('-created_at')
    all_items = List.objects.filter(owner=request.user).order_by('-pk')
    return render(request, 'home.html', {'all_items': all_items})

class AddView(View):
    @method_decorator(login_required)
    def post(self, request):
        msg = ''
        msg_type = ''
        if request.method == 'POST':
            todo_user = List()
            todo_user.owner = request.user
            form = ListForm(request.POST, instance=todo_user)
            if form.is_valid():
                form.save()
                msg = 'Se agregó con éxito'
                msg_type = True
                form = ListForm()
            else:
                msg_type = False
                msg = 'Ocurrió un problema'
        context = {
            'form': form,
            'msg': msg,
            'msg_type': msg_type
        }
        return render(request, 'add.html', context)

    @method_decorator(login_required)
    def get(self, request):
        form = ListForm()

        context = { 'form': form }
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

class EditView(View):
    @method_decorator(login_required)
    def post(self, request, todo_id):
        item = List.objects.get(pk=todo_id)
        form = ListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('El item ha sido editado'))
            return redirect('home')
        else:
            context = {
                'item': item,
                'form': form
            }
            messages.error(request, ('Ha ocurrido un problema al editar.'))
            return render(request, 'edit.html', context)

    def get(self, request, todo_id):
        item = List.objects.get(pk=todo_id)
        context = { 'item': item }
        return render(request, 'edit.html', context)
