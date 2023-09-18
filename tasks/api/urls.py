from django.urls import path

from rest_framework.authtoken import views as AuthTokenView

from . import views

urlpatterns = [
    path('', AuthTokenView.obtain_auth_token),
    path('create-user/', views.UserCreateAPIView.as_view()),
    path('create-task/', views.AddNewTaskAPIVIEW.as_view()),
    path('update-task/<int:pk>/', views.TaskUpdateApiView.as_view()),
    path('user-task-list/', views.TaskListAPIView.as_view()),
    path('delete-task/<int:pk>/', views.TaskDeleteAPIView.as_view()),
    # path('task-details/<int:pk>/', views.TaskDetailsView.as_view(), name='task-details'),
]
