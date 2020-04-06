from rest_framework import serializers

from ..models import Todo, List


class TodoSerializer(serializers.ModelSerializer):

    creation_date = serializers.DateTimeField(format="%H:%M %d-%m", required=False, read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"


class ListSerializer(serializers.ModelSerializer):

    creation_date = serializers.DateTimeField(format="%H:%M %d-%m", read_only=True)
    todo = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = "__all__"
