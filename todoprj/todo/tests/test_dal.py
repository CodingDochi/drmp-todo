from django.test import TestCase
from todo.dal import ToDoDAL
from todo.models import ToDoList

class ToDoDALTest(TestCase):
    def setUp(self):
        self.dal = ToDoDAL()

    def test_create_todo_list(self):
        todo_list_id = self.dal.create_todo_list("Shopping")
        todo_list = ToDoList.objects.get(id=todo_list_id)
        self.assertEqual(todo_list.name, "Shopping")

    def test_get_todo_list(self):
        todo_list = ToDoList.objects.create(name="Shopping")
        result = self.dal.get_todo_list(todo_list.id)
        self.assertEqual(result["name"], "Shopping")
