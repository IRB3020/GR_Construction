from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ClientForm
from .models import Client


def index(request):
    active_clients = Client.objects.filter(status='Active')
    return render(request, 'gr_construction_web/index.html', {'active_clients': active_clients})


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save()
            return render(request, 'gr_construction_web/client_added.html', {'client': new_client})
    else:
        form = ClientForm()
    return render(request, 'gr_construction_web/add_client.html', {'form': form})


def client_added(request):
    return redirect('clients-list')


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'gr_construction_web/client_detail.html', {'client': client})


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


def clients_list(request):
    clients = Client.objects.filter(status='Active')
    return render(request, 'gr_construction_web/clients_list.html', {'clients': clients})


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


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients-list')
    return render(request, 'gr_construction_web/client_delete.html', {'client': client})
