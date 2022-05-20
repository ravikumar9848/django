from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.TaskList.as_view()),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-create/', views.taskCreate, name="task-Create"),
    path('task-delete/', views.taskDelete, name="task-delete"),
   
    
    ]