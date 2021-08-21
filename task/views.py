from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):
    all_tasks = Task.objects.all()
    return render(request, 'home.html', {"tasks":all_tasks})


def form(request):

    if request.method == "POST":
        name_field = request.POST['name']
        Task.objects.create(name=name_field)

        return redirect('form')

    else:
        return render(request, 'form.html')