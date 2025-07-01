from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'todo_list/login.html'
    redirect_authenticated_user = True
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo_list/task_list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo_list/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'todo_list/task_confirm_delete.html'