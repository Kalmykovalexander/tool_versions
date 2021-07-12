from rest_framework import serializers
from .models import Tool

# Serializer for display object attributes
class ToolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('name', 'version', 'stage')


# Serializer for Tool model
class ToolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'