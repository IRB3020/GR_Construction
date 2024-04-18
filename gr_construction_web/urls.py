from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.registerPage, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('add-client/', views.add_client, name='add-client'),
    path('client-added/', views.client_added, name='client-added'),
    path('client/<int:pk>/', views.client_detail, name='client-detail'),
    path('client/<int:pk>/edit/', views.client_form, name='client-edit'),
    path('clients/', views.clients_list, name='clients-list'),
    path('client/<int:pk>/edit/', views.client_edit, name='client-edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client-delete'),

]
