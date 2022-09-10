from asyncio import all_tasks
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolistV(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            
            # form in change for particular user in model
            form.save(commit=False).user = request.user
            form.save()
            
            
        messages.success(request,('New task added successfully'))
        return redirect('todolist')
    else:
    
        all_tasks = TaskList.objects.filter(user=request.user)
        
        # paginator from documentation
        paginator = Paginator(all_tasks, 5)
        page_number = request.GET.get('page')
        all_tasks = paginator.get_page(page_number)
        
        
        return render(request, 'todolist.html', {'all_tasks'  : all_tasks})
    

def task_edit(request, task_id):
    if request.method == 'POST':
        task_obj = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
        messages.success(request,('Task edited'))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj' : task_obj})
        

def task_delete(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.user == request.user:
        task.delete()
    else:
        messages.error(request, 'Restricted to access')
    return redirect('todolist')

def task_complete(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.user == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, 'Restricted to access')
    return redirect('todolist')

def task_pending(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.user == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, 'Restricted to access')
    return redirect('todolist')


def home(request):
    context = {
        "home_text" : "Wecome to home page",
    }
    return render(request, 'home.html', context)

def contactV(request):
    context = {
        "contact_text" : "Wecome to contact",
    }
    return render(request, 'contacts.html', context)


def aboutV(request):
    context = {
        "about_text" : "Wecome to about",
    }
    return render(request, 'about.html', context)

