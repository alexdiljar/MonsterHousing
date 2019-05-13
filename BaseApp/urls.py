from django.urls import path, include

from . import views

urlpatterns = [
    path('about_us/', views.about_us_index, name="about_us_index"),
    path('terms_and_conditions/', views.terms_index, name="terms_index"),
    path('', views.front_page_index, name="front_page_index"),
]
