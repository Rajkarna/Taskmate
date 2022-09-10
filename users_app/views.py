from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registration successful')
            return redirect('register')
    else:
    
        register_form = RegisterForm()
    return render(request, 'register.html', {'register_form': register_form})
    
