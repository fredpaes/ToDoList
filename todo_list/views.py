from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})
    else:
        return redirect('login')

def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ListForm(request.POST)
            
            if form.is_valid():
                form.save()
                # all_items = List.objects.all
                # messages.success(request, ('success'))
                # return render(request, 'home.html', {'all_items': all_items})
                return redirect('home')
        else:
            return render(request, 'add.html')
    else:
        return redirect('login')