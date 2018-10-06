from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

class Project(models.Model):
    semester=models.CharField(max_length=100)
    course_name=models.CharField(max_length=100)
    project_name=models.CharField(max_length=100)
    project_description=models.TextField(max_length=100)
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    like=models.IntegerField(max_length=100)
