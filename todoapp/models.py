from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField(default=False)
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)

class Todoto(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField(default=False)
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True) 