from django.db import models

# Create your models here.


class ToDoList(models.Model):
    task = models.CharField(max_length=200)