from django.db import models

class TodoItem(models.Model):
    content = models.CharField(max_length = 40)

    def __str__(self):
        return self.content
