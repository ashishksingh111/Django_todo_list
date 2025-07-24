from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# View all tasks and create new task
def index(request):
    tasks = Task.objects.all().order_by('-created')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'todo/index.html', {'tasks': tasks})

# Mark complete/incomplete
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.complete = not task.complete
    task.save()
    return redirect('/')

# Delete task
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('/')

def viewTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'todo/view.html', {'task': task})

def editTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task.title = title
            task.save()
        return redirect('/')
    return render(request, 'todo/edit.html', {'task': task})
