from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.catalog_index, name="catalog_index"),
    path('<int:id>/seller_profile', views.get_seller_profile, name="seller_profile"),
    path('<int:id>', views.get_property_by_id, name="property_details"),
    path('<int:id>/buy_property', include('Transactions.urls')),
    path('edit_property/<int:id>', views.edit_property, name='edit_property'),
    path('delete_property/<int:id>', views.delete_property, name='delete_property')
]
