from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('/new', views.creation),
    path('/create', views.addShow),
    path('/<int:show_id>', views.viewShow),
    path('/<int:show_id>/edit', views.editShow),
    path('/<int:show_id>/update', views.updateShow),
    path('/<int:show_id>/delete', views.deleteShow),

]