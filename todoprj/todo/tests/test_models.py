from django.test import TestCase
from todo.models import ToDoList

class ToDoListModelTest(TestCase):
    def test_create_todo_list(self):
        todo_list = ToDoList.objects.create(name="Shopping")
        self.assertEqual(todo_list.name, "Shopping")
