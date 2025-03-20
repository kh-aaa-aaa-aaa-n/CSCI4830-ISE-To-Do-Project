from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "todos")
    text = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text
