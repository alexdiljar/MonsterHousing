from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
#    path('register2', views.register2, name='register2'),
    path('login', LoginView.as_view(template_name='User/SignIn.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('account', views.account, name='account'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('account_properties', views.get_all_user_properties, name='all_user_properties'),
    path('add_property', views.add_property, name='add_property'),
    path('transactions', include('Transactions.urls'))
]
