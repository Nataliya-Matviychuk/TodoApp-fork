from django.urls import path
from .views import (
    home, 
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    AskAIView, 
    ChatDeleteView,
)

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/create/', TaskCreate.as_view(), name='task-create'),
    path('task/update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task/delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('ask-ai/', AskAIView.as_view(), name='ask-ai'),
    path('delete-chat/', ChatDeleteView.as_view(), name='delete-chat'), 
]
