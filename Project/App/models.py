from django.db import models
from django.contrib.auth import User
class Project(models.Model):
    course_name=models.CharField(max_length=100)
    project_name=models.CharField(max_length=100)
    project_description=models.TextField(max_length=100)
    member=models.OneToManyField('User')
    date=models.DateField(default=datetime.now())
    like=model.ManyToManyField('User')

# Create your models here.
