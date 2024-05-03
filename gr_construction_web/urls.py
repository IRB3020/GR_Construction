from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.registerPage, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

    path('add-client/', views.add_client, name='add-client'),
    path('client-added/', views.client_added, name='client-added'),
    path('client/<int:pk>/', views.client_detail, name='client-detail'),
    path('client/<int:pk>/edit/', views.client_form, name='client-edit'),
    path('clients/', views.clients_list, name='clients-list'),
    path('client/<int:pk>/delete/', views.client_delete, name='client-delete'),

    path('worksites/add/', views.add_worksite, name='add-worksite'),
    path('worksite-added/', views.worksite_added, name='worksite-added'),
    path('worksites/<int:pk>/', views.worksite_detail, name='worksite-detail'),
    path('worksites/', views.worksite_list, name='worksite-list'),
    path('worksites/<int:pk>/edit/', views.worksite_form, name='worksite-edit'),
    path('worksites/<int:pk>/delete/', views.worksite_delete, name='worksite-delete'),

    path('worksites/<int:worksite_id>/bills/', views.bill_list, name='bill-list'),
    path('bills/<int:pk>/', views.bill_detail, name='bill-detail'),
    path('worksites/<int:worksite_id>/bills/<int:pk>/edit/', views.bill_form, name='bill-edit'),
    path('worksites/<int:worksite_id>/bills/add/', views.add_bill, name='add-bill'),
    path('worksites/<int:worksite_id>/bill-added/', views.bill_added, name='bill-added'),
    path('bills/<int:bill_id>/delete/', views.bill_delete, name='bill-delete'),
    path('bills/<int:pk>/edit/', views.bill_edit, name='bill-edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
