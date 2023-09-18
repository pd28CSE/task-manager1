from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import UserSerializer, TaskSerializer
from . permissions import TaskUpdatePermission

from .. models import Task, TaskImage


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, ]



class AddNewTaskAPIVIEW(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = TaskSerializer
    parser_classes = [MultiPartParser, FormParser, ]

    def perform_create(self, serializer):
        images_data = self.request.FILES.getlist('images')
        task = serializer.save(user=self.request.user)
        for image_data in images_data:
            image = TaskImage.objects.create(image=image_data, task=task)
            task.images.add(image)


class TaskUpdateApiView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [TaskUpdatePermission, ]
    serializer_class = TaskSerializer
    parser_classes = [MultiPartParser, FormParser, ]
    queryset = Task.objects.all()

    def perform_update(self, serializer):
        task = serializer.save()
        images_data = self.request.FILES.getlist('images') 
        if images_data:
            task.images.clear()
            for image in images_data:
                image = TaskImage.objects.create(image=image)
                task.images.add(image)


class TaskListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = user.usertask.all().order_by('-creationDateTime')
        return queryset


class TaskDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [TaskUpdatePermission, ]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetailsAPIView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [TaskUpdatePermission, ]
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'pk'
    queryset = Task.objects.all()

