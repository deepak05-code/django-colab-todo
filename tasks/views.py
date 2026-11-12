from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Task

@csrf_exempt
def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("home")
        
    all_tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": all_tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggles True/False
    task.save()                          # Saves the change to SQLite
    return redirect("home")

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()                        # Deletes the row from SQLite
    return redirect("home")
