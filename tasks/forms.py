
from django.forms import ModelForm
from .models import ProjectMember, Task , Project , Comment

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['Name', 'description']



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','Status','priority']

class CommentForm(ModelForm):
     class Meta:
        model = Comment
        fields = ['content', 'user', 'task']  
  

class ProjectMemberForm(ModelForm):
    class Meta:
        model = ProjectMember
        fields = ['Project','user' ,'Role']   
       
