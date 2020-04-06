from django.db import models

# Create your models here.


class List(models.Model):
    title = models.CharField(max_length=50, unique=True)
    importannt = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Todo(models.Model):

    message = models.CharField(max_length=70)
    todo_list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="todo")
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
