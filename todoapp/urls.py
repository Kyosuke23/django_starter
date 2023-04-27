from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('task_list/', TaskList.as_view(), name='task_list'),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('task_edit/<int:pk>/', TaskUpdate.as_view(), name='task_edit'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]
