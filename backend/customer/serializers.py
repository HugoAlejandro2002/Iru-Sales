from rest_framework import serializers
from .models import Customer, Note

from team.serializers import UserSerializer

class CustomerSeraializer(serializers.ModelSerializer):
    assigned_to = UserSerializer( read_only = True)
    
    class Meta:
        model =Customer
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at'
        )
        fields = (
            'id',
            'name',
            'contact_person',  
            'email', 
            'phone',
            'website',
            'assigned_to',
            'created_at',
            'modified_at'
        )

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'name',
            'body',
        )