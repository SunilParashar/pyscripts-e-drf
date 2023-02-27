
from django.urls import path
from . import views

urlpatterns = [
    path("todo/", views.TodoView.as_view(), name='todo'),
]
