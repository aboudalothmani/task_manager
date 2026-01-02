from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.task_list, name="task_list"),
    path("task/add/", views.task_create, name="task_create"),
    path("task/<int:pk>/edit/", views.task_update, name="task_update"),
    path("task/<int:pk>/delete/", views.task_delete, name="task_delete"),
    path("task/<int:pk>/toggle/", views.toggle_complete, name="task_toggle"),
]
