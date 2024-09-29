from django.urls import path
from todo.views import ToDoListView, ToDoListDetailView, ToDoItemView, ToDoItemCheckedStateView

urlpatterns = [
    path('lists/', ToDoListView.as_view(), name='todo-list'),
    path('lists/<str:list_id>/', ToDoListDetailView.as_view(), name='todo-list-detail'),
    path('lists/<str:list_id>/items/', ToDoItemView.as_view(), name='todo-item'),
    path('lists/<str:list_id>/items/<str:item_id>/', ToDoItemView.as_view(), name='todo-item-detail'),
    path('lists/<str:list_id>/checked_state/', ToDoItemCheckedStateView.as_view(), name='todo-item-checked-state'),
]
