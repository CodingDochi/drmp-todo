from django.db import models
from uuid import uuid4

class ToDoList(models.Model):
    name = models.CharField(max_length=255)

    def item_count(self):
        return self.items.count()

    def __str__(self):
        return self.name

class ToDoListItem(models.Model):
    todo_list = models.ForeignKey(ToDoList, related_name='items', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    checked = models.BooleanField(default=False)
    item_id = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.label
