from django.urls import path
from .views import todolistV, contactV, aboutV,task_delete,task_edit, task_complete, task_pending

urlpatterns = [
    path('', todolistV, name="todolist"),
    path('delete/<task_id>/', task_delete, name="delete"),
    path('edit/<task_id>/', task_edit, name="edit"),
    path('complete/<task_id>/', task_complete, name="complete"),
    path('pending/<task_id>/', task_pending, name="pending"),
   
]
