from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.payment_information_purchase, name='user_information_purchase'),
    # path('payment_information', views.payment_information_purchase, name='payment_information_purchase'),
    # path('review_purchase', views.review_purchase, name='review_purchase'),
    # path('confirm_purchase', views.confirm_purchase, name='confirm_purchase')
]