from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='User/SignIn.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('account', views.account, name='account'),
    path('add_property', views.create_property, name="create_property"),
    path('account_properties', views.account_properties, name='account_properties'),
    path('transactions', include('Transactions.urls')),
    path('edit_property/<int:id>', views.edit_property, name='edit_property'),

]
