from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm
from . import models
from . import forms
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})

def edit_task(request, pk):
    task = models.TaskModel.objects.get(pk=pk)
    task_form = forms.TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/add_task.html', {'form': form})

def delete_task(request, pk):
    task = models.TaskModel.objects.get(pk=pk)
    task.delete()
    return redirect('show_tasks')

def complete_task(request, pk):
    task = models.TaskModel.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')
