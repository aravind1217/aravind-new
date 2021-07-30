from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CrudUser
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from .forms import CrudForm, UserRegisterForm, CrudUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CrudView(ListView):
    model = CrudUser
    template_name = 'crud.html'
    context_object_name = 'users'


@login_required
def newform(request):
    if request.method == 'POST':
        form = CrudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your form has been created ')

            return redirect('list')

    else:
        form = CrudForm()
    return render(request, 'adduser.html', {'form': form})


@login_required
def CrudNewdetail(request, id):
    a = CrudUser.objects.get(id=id)
    return render(request, 'detail.html', {'a': a})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def update(request, id):
    a = CrudUser.objects.get(id=id)
    if request.method == 'POST':
        update = CrudUpdateForm(request.POST, request.FILES, instance=a)
        if update.is_valid():
            update.save()

            messages.success(request, f'Your account has been updated')

            return redirect('list')
    else:
        update = CrudUpdateForm()
    return render(request, 'update.html', {'update': update})


class DeleteCrudUser(View, LoginRequiredMixin):
    def get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
