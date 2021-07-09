from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=150)
    stage = models.IntegerField(default=1)
    version = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
