from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from django.db.models import Q

from .forms import UserCreationForm
from . models import Task, TaskImage

# Create your views here.


class UserCreationsView(View, LoginRequiredMixin):

    template_name = 'create_user.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('tasks:task-list'))
        form = UserCreationForm()
        content = {'form': form}
        return render(request, self.template_name, context=content)
    

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account creation successful. Now you can login.")
            return HttpResponseRedirect(reverse('tasks:user-create'))
        
        content = {'form': form}
        return render(request, self.template_name, context=content)


class UserLogin(View):

    template_name = 'login_user.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('tasks:task-list'))
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        requestData = request.POST
        userName = requestData.get('username')
        password = requestData.get('password')
        user = authenticate(username=userName, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tasks:task-list'))
        
        messages.error(request, "Username or password is incorrect.")
        content = {'username': userName, 'password': password}
        return render(request, self.template_name, context=content)


def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('tasks:login-user'))



class UserTaskListView(LoginRequiredMixin, generic.ListView):
    login_url = '/account-login/'
    template_name = 'user_task_list.html'
    context_object_name = 'user_task_list'

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user).order_by('-creationDateTime')
        return queryset


class TaskDetailsView(LoginRequiredMixin, generic.View):
    login_url = '/account-login/'
    template_name = 'task_details.html'

    def get(self, request, *args, **kwargs):
        taskId  = kwargs.get('pk')
        user = self.request.user
        try:
            task = Task.objects.get(pk=taskId, user=user)
        except Task.DoesNotExist:
            task = Task.objects.none
        content = {'task': task}
        return render(request, self.template_name, context=content)


class DeleteTask(LoginRequiredMixin, generic.View):
    login_url = '/account-login/'

    def get(self, request, *args, **kwargs):
        taskId  = kwargs.get('pk')
        user = self.request.user
        try:
            task = Task.objects.get(pk=taskId, user=user)
            task.images.all().delete()
            task.delete()
            messages.success(request, 'Task delete successfull.')
        except Task.DoesNotExist:
            task = Task.objects.none
            messages.success(request, 'You have no permissions to delete this task.')
        return HttpResponseRedirect(reverse('tasks:task-list'))


class TaskUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/account-login/'
    template_name = 'task_update.html'
    
    def get_success_url(self):
        return reverse('tasks:task-update-view', args=(self.kwargs['pk'],))

    model = Task
    fields = ['title', 'description', 'images', 'dueDate', 'priority', 'isCompleted', ]



class TaskCreate(LoginRequiredMixin, generic.View):
    login_url = '/account-login/'
    template_name = 'create_task.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

    def post(self, request, *args, **kwargs):
        data = request.POST
        title = data['title']
        description = data['description']
        pri = data['priority']
        dueDate = data['dueDate']
        isCompleted = data.get('isComplete', False)
        user = request.user

        task = Task.objects.create(user=user, title=title, description=description, dueDate=dueDate, priority=pri, isCompleted=isCompleted)

        files = request.FILES.getlist('image')
        for imageFile in files:
            image = TaskImage.objects.create(image=imageFile)
            task.images.add(image)
        
        messages.success(request, 'Task added successful.')
        return render(request, self.template_name)


class TaskFilterView(UserTaskListView):

    def get_queryset(self):
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        user = self.request.user
        queryset = Task.objects.filter(Q(user=user) & Q(priority=priority) | Q(isCompleted=status))
        return queryset


class TaskSearchView(UserTaskListView):

    def get_queryset(self):
        title = self.request.GET.get('title')
        user = self.request.user
        queryset = Task.objects.filter(user=user, title__icontains=title)
        return queryset


# python manage.py dumpdata --indent=2 > fixtures/tasklist.json