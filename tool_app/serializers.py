from rest_framework import serializers
from .models import Tool


class ToolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('name', 'version', 'stage')


class ToolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'