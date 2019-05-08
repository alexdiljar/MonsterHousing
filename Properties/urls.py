from django.urls import path

from . import views

urlpatterns = [
    path('', views.properties, name="properties"),
    path('<int:id>', views.get_properties_by_id, name="property_details"),
]
