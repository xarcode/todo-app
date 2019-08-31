from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def index(request):
    items = TodoItem.objects.all()
    return render(request, 'todo.html', {'item_list': items})

def addItem(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def deleteItem(request, todo_id):
    del_item = TodoItem.objects.get(id=todo_id)
    del_item.delete()
    return HttpResponseRedirect('/')
