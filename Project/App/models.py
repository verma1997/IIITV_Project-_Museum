from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime



class Project(models.Model):
    CHOICES=(('ONE','I'),
            ('TWO','II'),
            ('THREE','III'),
            ('FOUR','IV'),
            ('FIVE','V'),
            ('SIX','VI'),
            ('SEVEN','VII'),
            ('EIGHT','VIII'),)
    semester=models.CharField(max_length=100,choices=CHOICES,default='ONE')
    course_name=models.CharField(max_length=100)
    project_name=models.CharField(max_length=100)
    project_description=models.TextField(max_length=100)
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    like=models.IntegerField(default=0)



    def __str__(self):
        return self.semester + "  " + self.course_name + " " + self.project_name
