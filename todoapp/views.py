from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse

#factory
class todo():

    def obj(id):
        return Todo.objects.get(id=id)
    def all():
        return Todo.objects.all()


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
    mydictionary = {
        "alltodos" : todo.all()
    }
    return render(request,'list.html',context=mydictionary)

def delete(request,id):
    obj = todo.obj(id)
    obj.delete()
    mydictionary = {
        "alltodos" : todo.all()
    }
    return render(request,'list.html',context=mydictionary)

def deleteAll(request):
    obj = todo.all()
    obj.delete()
    mydictionary = {
        "alltodos" : todo.all()
    }
    return render(request,'list.html',context=mydictionary)

def done(request,id):
    obj = todo.obj(id)
    obj.done = True
    obj.priority = 0
    obj.save()
    mydictionary = {
        "alltodos" : todo.all()
    }
    return render(request,'list.html',context=mydictionary)

def list(request):
    mydictionary = {
        "alltodos" : todo.all()
    }
    return render(request,'list.html',context=mydictionary)

def sortdata(request):
    mydictionary ={
        "alltodos" : todo.all().order_by('-priority')
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
    mydictionary = {
        "alltodos" : todo.all()
    }
    return render(request,'list.html',context=mydictionary)