from rest_framework import serializers
from .models import ToDoList, ToDoListItem

class ToDoListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoListItem
        fields = ['id', 'label', 'checked']

class ToDoListSerializer(serializers.ModelSerializer):
    items = ToDoListItemSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoList
        fields = ['id', 'name', 'items', 'item_count']