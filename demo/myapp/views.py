from django.shortcuts import render , HttpResponse
from .models import toDoItem
# Create your views here.

def home(request):
    return render(request,"home.html")

def todos(request):
    items = toDoItem.objects.all()
    return render(request,"toDo.html",{"todos": items})

   