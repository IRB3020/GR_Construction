from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ClientForm, CreateUserForm
from .models import Client, Manager
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    active_clients = Client.objects.filter(status='Active')
    return render(request, 'gr_construction_web/index.html', {'active_clients': active_clients})


@login_required(login_url='login')
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save()
            return render(request, 'gr_construction_web/client_added.html', {'client': new_client})
    else:
        form = ClientForm()
    return render(request, 'gr_construction_web/add_client.html', {'form': form})


@login_required(login_url='login')
def client_added(request):
    return redirect('clients-list')


@login_required(login_url='login')
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'gr_construction_web/client_detail.html', {'client': client})


@login_required(login_url='login')
def client_form(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients-list')  # Redirect to the list of clients
    else:
        form = ClientForm(instance=client)
    return render(request, 'gr_construction_web/client_form.html', {'form': form})


@login_required(login_url='login')
def clients_list(request):
    clients = Client.objects.filter(status='Active')
    return render(request, 'gr_construction_web/clients_list.html', {'clients': clients})


@login_required(login_url='login')
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients-list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'gr_construction_web/client_edit.html', {'form': form})


@login_required(login_url='login')
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients-list')
    return render(request, 'gr_construction_web/client_delete.html', {'client': client})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='Project Manager')
                user.groups.add(group)
                manager = Manager.objects.create(user=user,)
                manager.save()

                messages.success(request, 'Account Created For: ' + username)
                return redirect('login')
        context = {'form': form}
        return render(request, 'registration/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect!')
        context = {}
        return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return render(request, 'registration/logout.html')
