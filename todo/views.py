
#views component
#1.function based
#2.class Based
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskEdit
def update(request,id):
  todo=Task.objects.get(todo_id=id)
  if request.method=="GET":
    context={
      "todo_text":todo.todo_text,
      "id":id,
    }
    return render(request,'edit.html',context)
  elif request.method=='POST':
    todo_value=request.POST.get('todo_text')
    Task.objects.filter(todo_id=id).update(todo_text=todo_value)
    return redirect('/')

  
def home(request):
  todos=Task.objects.all()
  context={
    'todos':todos
  }
  return render(request,'todo.html',context)
  

def delete(request,id):
  todo=Task.objects.get(todo_id=id)
  todo.delete()
  return redirect('/')

def add(request):
  if request.method=='POST':
    if request.POST.get('todo_text').strip()!="":
      text=request.POST.get("todo_text")
      form=Task.objects.create(todo_text=text)
      return redirect('/')
    else:
      return redirect('/')
  

  #CSS,JavaScript,JQuery,Images
  #####Static Cheazen during the life of website 
  ###static 
  ###CSS
  ###javaScript
  ###images
  