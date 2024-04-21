from django import forms
from django.forms import ModelForm
from .models import Client, Manager, WorkSite, Bill
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'status', 'email', 'phone_number', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].label = 'Phone Number (including area code)'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ['name', 'email', 'phone_number']
        exclude = ['user']


class WorkSiteForm(forms.ModelForm):
    class Meta:
        model = WorkSite
        fields = ['title', 'address', 'description', 'client', 'finished_image']


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['title', 'amount', 'date']
