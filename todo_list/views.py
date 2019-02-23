from django.shortcuts import render
from .models import *
from .forms import ListForm

# Create your views here.
def home(request):
    all_items = List.objects.all
    return render(request, 'home.html', {'todos': all_items})

def add(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added to list!'))
            return render(request, 'add.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'add.html', {'all_items': all_items})