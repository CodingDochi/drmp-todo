from django.test import TestCase
from todo.serializers import ToDoListSerializer, ToDoListItemSerializer
from todo.models import ToDoList, ToDoListItem

class ToDoListSerializerTest(TestCase):
    def test_valid_serializer(self):
        todo_list = ToDoList.objects.create(name="Shopping")
        serializer = ToDoListSerializer(todo_list)
        self.assertEqual(serializer.data['name'], "Shopping")

    def test_valid_item_serializer(self):
        todo_list = ToDoList.objects.create(name="Shopping")
        item = ToDoListItem.objects.create(todo_list=todo_list, label="Buy milk", checked=False)
        serializer = ToDoListItemSerializer(item)
        self.assertEqual(serializer.data['label'], "Buy milk")
