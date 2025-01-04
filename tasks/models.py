from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  STATUS_CHOICES = [
        ('TO_DO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]
  Status = models.TextField(  max_length=12, 
        choices=STATUS_CHOICES, 
        default='TO_DO' )
  PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ] 
  priority = models.CharField(
        max_length=7, 
        choices=PRIORITY_CHOICES, 
        default='LOW' 
    )
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title + ' - ' + self.user.username 
    


class Project(models.Model):
  Name = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.Name + ' - ' + self.user.username 
  

    
class ProjectMember(models.Model):
     Project = models.ForeignKey(Project, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     ROLE_CHOICES = [
        ('ADMIN', 'ADMIN'),
        ('MEMBER', 'MEMBER'),
     ]
     Role = models.TextField(  max_length=12, 
        choices=ROLE_CHOICES, 
        default='MEMBER' )
     created = models.DateTimeField(auto_now_add=True)
     datecompleted = models.DateTimeField(null=True, blank=True)

     def __str__(self):
      return self.Role + ' - ' + self.user.username
      
  
class Comment(models.Model):
  content = models.CharField(max_length=200) 
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return self.user + ' - ' + self.user.username 
  
    
    


   