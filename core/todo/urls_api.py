from django.urls import path, include
from . import views
urlpatterns = [
    path("api/todo/", views.TodoView.as_view(), name='todo_api'),
]
