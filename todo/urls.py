from django.urls import path
from . import views
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView

urlpatterns = [
    path('task-list/', TaskList.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('task-detail/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('register/',views.register_fun, name='register'),
    path('login/',views.login_fun,name='login')

    #path('login/', CustomLoginView.as_view(), name='login')
]
