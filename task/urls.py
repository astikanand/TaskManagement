from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^all-tasks/$', views.TaskIndexView.as_view(), name='allTasks'),
    url(r'^my-tasks/$', views.MyTaskView.as_view(), name='myTasks'),
    url(r'^new-task/$', views.CreateTaskView.as_view(), name='newTask'),
    url(r'^(?P<taskid>\d+)/detail/$',views.taskDetail, name='taskDetail'),
    url(r'^(?P<taskid>\d+)/edit/$',views.UpdateTaskView.as_view(), name='editTask'),
    url(r'^(?P<taskid>\d+)/delete/$',views.DeleteTaskView.as_view(), name='deleteTask'),
]
