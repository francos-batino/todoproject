from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse

#factory
class todo():

    def obj(id):
        return Todo.objects.get(id=id)
    def dictionary():
        mydictionary = {
            "alltodos" : Todo.objects.all()
        }
        return mydictionary


# Create your views here.
def index(request):
    return render(request,'index.html')

def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.done = False
    obj.save()
    return render(request,'list.html',context=todo.dictionary())

def delete(request,id):
    obj = todo.obj(id)
    obj.delete()
    return render(request,'list.html',context=todo.dictionary())

def deleteAll(request):
    obj = todo.all()
    obj.delete()
    return render(request,'list.html',context=todo.dictionary())

def done(request,id):
    obj = todo.obj(id)
    obj.done = True
    obj.priority = 0
    obj.save()
    return render(request,'list.html',context=todo.dictionary())

def list(request):
    return render(request,'list.html',context=todo.dictionary())

def sortdata(request):
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('-priority')
    }
    return render(request,'list.html',context=mydictionary)

def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos" : Todo.objects.filter(title__contains=q)
    }
    return render(request,'list.html',context=mydictionary)

def edit(request,id):
    obj = todo.obj(id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "priority" : obj.priority,
        "id" : obj.id,
        "done" : obj.done
    }
    return render(request,'edit.html',context=mydictionary)

def update(request,id):
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.done = request.GET['done']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    return render(request,'list.html',context=todo.dictionary())