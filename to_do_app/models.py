from django.db import models

# Create your models here.
class task(models.Model):
    task_name = models.CharField(max_length=64)
    completion_time =models.FloatField()
    created_at  = models.DateTimeField()
    updated_at =models.DateTimeField()

    def __str__(self):
        return self.task_name


