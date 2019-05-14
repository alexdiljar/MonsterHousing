from django.urls import path

from . import views

urlpatterns = [
    path('', views.catalog_index, name="catalog_index"),
    path('<int:id>/seller_profile', views.get_seller_profile, name="seller_profile"),
    path('<int:id>/buy_property', views.buy_property, name="buy_property"),
    path('<int:id>', views.get_properties_by_id, name="property_details"),
    path('<int:id>/buy_property/information', views.buy_property, name="buy_property"),
]
