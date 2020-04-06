from .serializer import TodoSerializer, ListSerializer
from ..models import Todo, List

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListTodoListCreateAPIView(ListCreateAPIView):

    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListTodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = List.objects.all()
    serializer_class = ListSerializer


class TodoListCreateAPIView(ListCreateAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

