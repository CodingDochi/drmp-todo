from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDoList, ToDoListItem
from .serializers import ToDoListSerializer, ToDoListItemSerializer
from .dal import ToDoDAL

todo_dal = ToDoDAL()

class ToDoListView(APIView):
    
    def get(self, request):
        todo_lists = todo_dal.list_todo_lists()
        return Response(todo_lists)

    def post(self, request):
        name = request.data.get('name')
        todo_list_id = todo_dal.create_todo_list(name)
        return Response({'id': todo_list_id, 'name': name}, status=status.HTTP_201_CREATED)


class ToDoListDetailView(APIView):
    
    def get(self, request, list_id):
        todo_list = todo_dal.get_todo_list(list_id)
        if todo_list:
            return Response(todo_list)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, list_id):
        success = todo_dal.delete_todo_list(list_id)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ToDoItemView(APIView):

    def post(self, request, list_id):
        label = request.data.get('label')
        todo_list = todo_dal.create_item(list_id, label)
        if todo_list:
            return Response(todo_list, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, list_id, item_id):
        todo_list = todo_dal.delete_item(list_id, item_id)
        if todo_list:
            return Response(todo_list)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ToDoItemCheckedStateView(APIView):

    def patch(self, request, list_id):
        item_id = request.data.get('item_id')
        checked_state = request.data.get('checked_state')
        todo_list = todo_dal.set_checked_state(list_id, item_id, checked_state)
        if todo_list:
            return Response(todo_list)
        return Response(status=status.HTTP_404_NOT_FOUND)