from django.urls import path

from . import views

urlpatterns = [
    path('', views.catalog_index, name="catalog_index"),
    path('<int:id>', views.get_properties_by_id, name="property_details"),
]
