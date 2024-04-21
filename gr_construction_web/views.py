from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ClientForm, CreateUserForm, WorkSiteForm, BillForm
from .models import Client, Manager, WorkSite, Bill
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
            return redirect('clients-list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'gr_construction_web/client_form.html', {'form': form})


@login_required(login_url='login')
def clients_list(request):
    clients = Client.objects.all()
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


@login_required(login_url='login')
def worksite_list(request):
    worksites = WorkSite.objects.all()
    return render(request, 'gr_construction_web/worksite_list.html', {'worksites': worksites})


@login_required(login_url='login')
def worksite_detail(request, pk):
    worksite = get_object_or_404(WorkSite, pk=pk)
    return render(request, 'gr_construction_web/worksite_detail.html', {'worksite': worksite})


@login_required(login_url='login')
def worksite_form(request, pk=None):
    if pk:
        worksite = get_object_or_404(WorkSite, pk=pk)
    else:
        worksite = None

    if request.method == 'POST':
        form = WorkSiteForm(request.POST, request.FILES, instance=worksite)
        if form.is_valid():
            worksite = form.save()
            return redirect('worksite-detail', pk=worksite.pk)
    else:
        form = WorkSiteForm(instance=worksite)

    return render(request, 'gr_construction_web/worksite_form.html', {'form': form})


@login_required(login_url='login')
def add_worksite(request):
    if request.method == 'POST':
        form = WorkSiteForm(request.POST)
        if form.is_valid():
            new_site = form.save()
            return render(request, 'gr_construction_web/worksite_added.html', {'worksite': new_site})
    else:
        form = WorkSiteForm()
    return render(request, 'gr_construction_web/add_worksite.html', {'form': form})


@login_required(login_url='login')
def worksite_added(request):
    return redirect('worksite-list')


@login_required(login_url='login')
def worksite_edit(request, pk):
    worksite = get_object_or_404(WorkSite, pk=pk)
    if request.method == 'POST':
        form = WorkSiteForm(request.POST, instance=worksite)
        if form.is_valid():
            form.save()
            return redirect('worksite-list')
    else:
        form = WorkSiteForm(instance=worksite)
    return render(request, 'gr_construction_web/worksite_edit.html', {'form': form})


@login_required(login_url='login')
def worksite_delete(request, pk):
    worksite = get_object_or_404(WorkSite, pk=pk)
    if request.method == 'POST':
        worksite.delete()
        return redirect('worksite-list')
    return render(request, 'gr_construction_web/worksite_delete.html', {'worksite': worksite})


@login_required(login_url='login')
def bill_list(request, worksite_id):
    worksite = get_object_or_404(WorkSite, pk=worksite_id)
    bills = worksite.bills.all()
    context = {
        'bills': bills,
        'worksite': worksite
    }
    return render(request, 'gr_construction_web/bill_list.html', context)


@login_required(login_url='login')
def bill_detail(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    context = {
        'bill': bill,
        'worksite_id': bill.worksite.id
    }
    return render(request, 'gr_construction_web/bill_detail.html', context)


@login_required(login_url='login')
def bill_form(request, pk=None):
    if pk:
        bill = get_object_or_404(Bill, pk=pk)
    else:
        bill = None

    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            bill = form.save()
            return redirect('bill-detail', pk=bill.pk)
    else:
        form = BillForm(instance=bill)
    return render(request, 'gr_construction_web/bill_form.html', {'form': form})


@login_required(login_url='login')
def add_bill(request, worksite_id):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.worksite_id = worksite_id
            bill.save()
            return redirect('bill-added', worksite_id=worksite_id)
    else:
        form = BillForm()
    return render(request, 'gr_construction_web/add_bill.html', {'form': form})


@login_required(login_url='login')
def bill_added(request, worksite_id):
    new_bill = Bill.objects.filter(worksite_id=worksite_id).latest('id')
    return render(request, 'gr_construction_web/bill_added.html', {'worksite_id': worksite_id, 'new_bill': new_bill})


@login_required(login_url='login')
def bill_delete(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill-list', worksite_id=bill.worksite.id)
    return render(request, 'gr_construction_web/bill_delete.html', {'bill': bill})


@login_required(login_url='login')
def bill_edit(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill-list', worksite_id=bill.worksite.id)
    else:
        form = BillForm(instance=bill)
    return render(request, 'gr_construction_web/bill_edit.html', {'form': form})
