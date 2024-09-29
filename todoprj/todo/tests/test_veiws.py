from django.test import TestCase
from django.urls import reverse
from todo.models import ToDoList

class ToDoListViewTest(TestCase):
    def test_get_all_lists(self):
        ToDoList.objects.create(name="Shopping")
        response = self.client.get(reverse('todo-list'))  # 뷰의 URL 네임스페이스에 맞춰 변경
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shopping")

    def test_create_todo_list(self):
        response = self.client.post(reverse('todo-list'), {"name": "Shopping"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ToDoList.objects.count(), 1)
        self.assertEqual(ToDoList.objects.first().name, "Shopping")

    def test_delete_todo_list(self):
        todo_list = ToDoList.objects.create(name="Shopping")
        response = self.client.delete(reverse('todo-list-detail', args=[todo_list.id]))  # 상세 URL에 맞춤
        self.assertEqual(response.status_code, 204)
        self.assertEqual(ToDoList.objects.count(), 0)
