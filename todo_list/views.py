from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def add(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        
        if form.is_valid():
            form.save()
            # all_items = List.objects.all
            # messages.success(request, ('success'))
            # return render(request, 'home.html', {'all_items': all_items})
            return HttpResponseRedirect('home')
    else:
        return render(request, 'add.html')