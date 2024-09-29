from .models import ToDoList, ToDoListItem
from django.core.exceptions import ObjectDoesNotExist

class ToDoDAL:
    
    def list_todo_lists(self):
        todo_lists = ToDoList.objects.all().order_by('name')
        return [
            {
                "id": str(todo_list.id),
                "name": todo_list.name,
                "item_count": todo_list.item_count()
            }
            for todo_list in todo_lists
        ]

    def create_todo_list(self, name: str) -> str:
        todo_list = ToDoList.objects.create(name=name)
        return str(todo_list.id)

    def get_todo_list(self, id: str):
        try:
            todo_list = ToDoList.objects.get(id=id)
            return {
                "id": str(todo_list.id),
                "name": todo_list.name,
                "items": [
                    {
                        "id": str(item.item_id),
                        "label": item.label,
                        "checked": item.checked
                    }
                    for item in todo_list.items.all()
                ]
            }
        except ObjectDoesNotExist:
            return None

    def delete_todo_list(self, id: str) -> bool:
        try:
            todo_list = ToDoList.objects.get(id=id)
            todo_list.delete()
            return True
        except ObjectDoesNotExist:
            return False

    def create_item(self, todo_list_id: str, label: str):
        try:
            todo_list = ToDoList.objects.get(id=todo_list_id)
            item = ToDoListItem.objects.create(
                todo_list=todo_list, label=label, checked=False
            )
            return self.get_todo_list(todo_list_id)
        except ObjectDoesNotExist:
            return None

    def set_checked_state(self, todo_list_id: str, item_id: str, checked_state: bool):
        try:
            item = ToDoListItem.objects.get(todo_list__id=todo_list_id, item_id=item_id)
            item.checked = checked_state
            item.save()
            return self.get_todo_list(todo_list_id)
        except ObjectDoesNotExist:
            return None

    def delete_item(self, todo_list_id: str, item_id: str):
        try:
            item = ToDoListItem.objects.get(todo_list__id=todo_list_id, item_id=item_id)
            item.delete()
            return self.get_todo_list(todo_list_id)
        except ObjectDoesNotExist:
            return None
