from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    categories = models.ManyToManyField('category.TaskCategory', related_name='tasks')

    def __str__(self):
        return self.taskTitle
