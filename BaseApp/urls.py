from django.urls import path

from . import views

urlpatterns = [
    path('aboutus/', views.about_us_index, name="about_us_index"),
    path('catalog/', views.catalog_index, name="catalog_index"),
    path('terms_and_conditions/', views.terms_index, name="terms_index"),
    path('frontpage/', views.front_page_index, name="front_page_index"),
]