from django.contrib import admin
from django.urls import path
from tasks.views import home, complete_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
