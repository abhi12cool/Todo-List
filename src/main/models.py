from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return str(self.todo)
    