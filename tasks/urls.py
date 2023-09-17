from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.UserCreationsView.as_view(), name='user-create'),
    path('create-task/', views.TaskCreate.as_view(), name='task-create'),
    path('account-login/', views.UserLogin.as_view(), name='login-user'),
    path('logout/', views.userLogout, name='logout-user'),
    path('user-task-list/', views.UserTaskListView.as_view(), name='task-list'),
    path('user-task-list-filter/', views.TaskFilterView.as_view(), name='task-list-filter'),
    path('user-task-search/', views.TaskSearchView.as_view(), name='task-search'),
    path('task-details/<int:pk>/', views.TaskDetailsView.as_view(), name='task-details'),
    path('delete-task/<int:pk>/', views.DeleteTask.as_view(), name='task-delete'),
    path('update-task-view/<int:pk>/', views.TaskUpdate.as_view(), name='task-update-view'),
]
