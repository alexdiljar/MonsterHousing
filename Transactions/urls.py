from django.urls import path, include
from . import views

urlpatterns = [
    path('user_information', views.user_information_purchase, name='buy_property'),
    path('review_purchase', views.review_purchase, name='review_purchase'),
    path('confirm_purchase', views.confirm_purchase, name='confirm_purchase')
]
