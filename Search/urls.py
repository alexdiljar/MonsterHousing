from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.search),
    path('<int:id>', views.result)

]
