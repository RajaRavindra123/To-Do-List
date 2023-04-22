from django.shortcuts import render
from .models import TodoListItem


# Create your views here.
def home(request):
    all_todo_items = home 
    return render (request,"myapp/home.html", {'all_items':'all_todo_items'})