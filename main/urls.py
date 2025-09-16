from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="index"),
    path("tasks/<int:task_id>/toggle/", views.toggle_task, name="toggle_task"),
    path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
]
