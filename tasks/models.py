from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskImage(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.image)


class Task(models.Model):
    user = models.ForeignKey(User, related_name='usertask', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=255, blank=False)
    images = models.ManyToManyField(TaskImage)
    creationDateTime = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateField(blank=False)
    priority = models.CharField(
        max_length=7,
        blank=False,
        choices=(
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
        ),
    )
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.user, self.title)

    class Meta:
        unique_together = ('user', 'title')
