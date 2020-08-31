from .models import Task
from django.forms import ModelForm

class TaskEdit(ModelForm):
  class Meta:
    model=Task
    fields=['todo_text','todo_id']
