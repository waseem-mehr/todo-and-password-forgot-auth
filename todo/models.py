from django.db import models

# Create your models here.
class Task(models.Model):
  todo_id=models.AutoField(primary_key=True)
  todo_text=models.TextField(max_length=255,null=True)

  def __str__(self):
    return self.todo_text

