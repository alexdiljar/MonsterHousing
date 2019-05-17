from django.urls import path, include
from . import views

urlpatterns = [
    path('user_information', views.user_information_purchase, name='buy_property'),
    # path('payment_information', views.payment_information, name='payment_information'),
    # path('edit_information', views.edit_account, name ='edit_information')
    path('review_purchase', views.review_purchase, name='review_purchase')
    # path('confirm_purchase', views.confirm_purchase, name='confirm_purchase')
]