from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime
from django.utils.translation import ugettext_lazy as _

from enum import unique


SEMESTER=(('ONE','I'),
            ('TWO','II'),
            ('THREE','III'),
            ('FOUR','IV'),
            ('FIVE','V'),
            ('SIX','VI'),
            ('SEVEN','VII'),
            ('EIGHT','VIII'),)
    
COURSE_NAME = (('Introduction To Programming', 'Introduction To Programming'),
                ('Intro To Information Technology', 'Intro To Information Technology'),
                ('Information Society', 'Information Society'),
                ('Database Management System', 'Database Management System'),
                ('Operating System', 'Operating System'),
                ('Computer Networks', 'Computer Networks'),
                ('Software Engineering', 'Software Engineering'),
                ('Web Technology', 'Web Technology'),)

FACULTY = (('Dr Naveen Kumar','Dr Naveen Kumar'),
    ('Dr Manik Lal Das','Dr Manik Lal Das'),
    ('Dr P M Jat','Dr P M Jat'),
    ('Dr Ashish Phophalia','Dr Ashish Phophalia'),
    ('Dr Asim Banerjee','Dr Asim Banerjee'),
    ('Mr Santosh Bharti','Mr Santosh Bharti')
)

class Project(models.Model):
    semester=models.CharField(max_length=100, choices=SEMESTER, default='')
    course_name = models.CharField(max_length=100, choices=COURSE_NAME, default='Introduction To Programming')
    project_name=models.CharField(max_length=100, unique=True)
    project_description=models.TextField(max_length=500, unique=True)
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    # faculty = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faculty', null=False, default='')
    faculty = models.CharField(max_length=100, choices=FACULTY, default='')
    student_mentor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='student_mentor')
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    file_upload = models.FileField(blank=True, null=True, verbose_name=_("file"), upload_to='')

    class Meta:
       verbose_name = _("Project")
       verbose_name_plural = _("Projects")

    # def __init__(self, *args, **kwargs):
    #     # first call parent's constructor
    #     super(Project, self).__init__(*args, **kwargs)
    #     # there's a `fields` property now
    #     self.project_description['project_description'].required = False

    def __str__(self):
        return self.semester + "  " + self.course_name + " " + self.project_name

class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    kind = models.CharField(max_length=100, default="Mentor")

    class Meta:
        verbose_name = _("Relationship")
        verbose_name_plural = _("Relationships")

    def __str__(self):
        return str(
            self.from_user.name + " - " +
            self.to_user.name + " (" +
            self.kind.name + ")")
