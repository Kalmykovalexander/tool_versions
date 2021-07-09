from django.db import models


class Stage(models.Model):
    stage = models.CharField(max_length=50)

    def __str__(self):
        return self.stage


class Tool(models.Model):
    name = models.CharField(max_length=150)
    stage = models.ForeignKey(Stage, default=1, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
