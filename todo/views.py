from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Task
# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasklist.html'


class TaskCreate(CreateView):
    model = Task
    fields = '_all_'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'


class TaskUpdate(UpdateView):
    model = Task
    fields = '_all_'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'


class TaskDelete(DeleteView):
    model = Task
    fields = '_all_'
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskdetail.html'


def register_fun(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Your account has been created!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_fun(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Your account has been created!')
            return redirect('todo/task-list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})