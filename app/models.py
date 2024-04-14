from django.db import models

# Create your models here.


class Users(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.IntegerField()
    
task_choices=[
    ('PENDING', 'Pending'),
    ('DONE', 'Done')
]

class Task(models.Model):
    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    task_detail=models.TextField(max_length=200)
    task_type=models.CharField( max_length=50,choices=task_choices)
    
    