from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "roll", "joing", "updated")
        model = Note