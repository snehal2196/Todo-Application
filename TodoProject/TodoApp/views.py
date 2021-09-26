from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.

def todo(request):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todos/todo_list.html', context)


def insert_todo_item(request):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/')


def delete_todo(request, id=0):
    todo = Todo(pk=id)
    todo.delete()
    return redirect('/')
