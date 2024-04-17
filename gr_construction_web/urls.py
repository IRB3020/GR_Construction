from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('add-client/', views.add_client, name='add-client'),
    path('client-added/', views.client_added, name='client-added'),
    path('client/<int:pk>/', views.client_detail, name='client-detail'),
    path('client/<int:pk>/edit/', views.client_form, name='client-edit'),
    path('clients/', views.clients_list, name='clients-list'),
    path('client/<int:pk>/edit/', views.client_edit, name='client-edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client-delete'),

    path('accounts/', include('django.contrib.auth.urls')),
]
