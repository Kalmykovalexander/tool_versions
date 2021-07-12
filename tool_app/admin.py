from django.contrib import admin
from .models import Tool

# Admin Panel
class ToolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stage', 'version', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'stage', 'version')


admin.site.register(Tool, ToolAdmin)
