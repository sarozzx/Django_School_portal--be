from django.db import models
from users.models import User
# Create your models here.



class Assignment(models.Model):
    title=models.CharField(max_length=100)
    # Course_choices = (
    #     ("maths", "Maths"),
    #     ("english", "English"),
    #     ("science", "Science"),
    # )
    # course = models.CharField(max_length=20, choices=Course_choices)
    teacher=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class GAssignment(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    assignment=models.ForeignKey(Assignment,on_delete=models.SET_NULL,null=True,blank=True)
    grade=models.FloatField(default=0)

    def __str__(self):
        return self.student.username

class Choice(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Question(models.Model):
    question=models.CharField(max_length=200)
    choices=models.ManyToManyField(Choice)
    answer=models.ForeignKey(Choice,on_delete=models.CASCADE,related_name="answer",blank=True,null=True)
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE,related_name="questions",blank=True,null=True)
    order=models.SmallIntegerField(default=0)

    def __str__(self):
        return self.question

class checkassignment(models.Model):
    assignment=models.ForeignKey(Assignment,on_delete=models.SET_NULL,null=True,blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username

class feed(models.Model):

    feedtxt=models.CharField(max_length=500)

    created = models.CharField(max_length=50,blank=True)
    teacher=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher.username

def upload_path(instance,filename):
    return '/'.join(['assignment',str(instance.title),filename])

class assign(models.Model):
    title=models.CharField(max_length=50)
    hw=models.FileField(blank=True,null=True,upload_to=upload_path)

    def __str__(self):
        return self.title

def upload_path1(instance,filename):
    return '/'.join(['assignment', str(instance.assignment.title),'submitted' ,filename])

class assignsubmit(models.Model):
    assignment=models.ForeignKey(assign,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    hwsubmitted=models.FileField(blank=True,null=True,upload_to=upload_path1)




