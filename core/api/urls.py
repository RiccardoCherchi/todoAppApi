from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.TodoListCreateAPIView.as_view()),
    path('list/', views.ListTodoListCreateAPIView.as_view()),
    path('list/<int:pk>', views.ListTodoRetrieveUpdateDestroyAPIView.as_view()),
    path('todo/<int:pk>/', views.TodoRetrieveUpdateDestroyAPIView.as_view()),
]
