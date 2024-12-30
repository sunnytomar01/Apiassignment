from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task , Project , Comment, ProjectMember
from .forms import ProjectMemberForm, TaskForm , ProjectForm , CommentForm ,ProjectMember


# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})


def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    






@login_required
def projects(request):
    projects = Project.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'project.html', {"projects": projects})

@login_required
def projects_completed(request):
    projects = Project.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'project.html', {"projects": projects})


@login_required
def create_project(request):
    if request.method == "GET":
        return render(request, 'create_project.html', {"form": ProjectForm})
    else:
        try:
            form = ProjectForm(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'create_project.html', {"form":ProjectForm, "error": "Error creating project."})


@login_required
def project_detail(request,project_id):
    if request.method == 'GET':
        project = get_object_or_404(Project, pk=project_id, user=request.user)
        form = ProjectForm(instance=project)
        return render(request, 'project_detail.html', {'project': project, 'form': form})
    else:
        try:
           project = get_object_or_404(Project, pk=project_id, user=request.user)
           form = ProjectForm(request.POST, instance=project)
           form.save()
           return redirect('projects')
        except ValueError:
            return render(request, 'project_detail.html',
                           {'project': project, 'form': form, 'error': 'Error updating project.'})

@login_required
def complete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        project.datecompleted = timezone.now()
        project.save()
        return redirect('projects')

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id, user=request.user)
    if request.method == 'POST':
       project.delete()
       return redirect('projects')    
       


 
@login_required
def comments(request):
    comments = Comment.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'comment.html', {"comments": comments})

@login_required
def comments_completed(request):
    comments = Comment.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'comment.html', {"comments": comments})


@login_required
def create_comment(request):
    if request.method == "GET":
        return render(request, 'create_comment.html', {"form": CommentForm})
    else:
        try:
            form =CommentForm(request.POST)
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.save()
            return redirect('comments')
        except ValueError:
            return render(request, 'create_comment.html', {"form":CommentForm, "error": "Error creating comment."})


@login_required
def comment_detail(request,comment_id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
        form = CommentForm(instance=comment)
        return render(request, 'comment_detail.html', {'comment': comment, 'form': form})
    else:
        try:
           comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
           form = CommentForm(request.POST, instance=comment)
           form.save()
           return redirect('comments')
        except ValueError:
            return render(request, 'comment_detail.html',
                           {'comment': comment, 'form': form, 'error': 'Error updating comment.'})

@login_required
def complete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == 'POST':
        comment.datecompleted = timezone.now()
        comment.save()
        return redirect('comments')

@login_required
def delete_comment(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == 'POST':
       comment.delete()
       return redirect('comments')    







        
@login_required
def projectmembers(request):
    projectmembers = ProjectMember.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'projectmember.html', {"projectmembers": projectmembers})

@login_required
def projectmembers_completed(request):
    projectmembers = projectmembers.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'projectmember.html', {"projectmembers":projectmembers})


@login_required
def create_projectmember(request):
    if request.method == "GET":
        return render(request, 'create_projectmember.html', {"form": ProjectMemberForm})
    else:
        try:
            form =ProjectMemberForm(request.POST)
            new_projectmember = form.save(commit=False)
            new_projectmember.user = request.user
            new_projectmember.save()
            return redirect('projectmembers')
        except ValueError:
            return render(request, 'create_comment.html', {"form":ProjectMemberForm, "error": "Error creating projectmember."})


@login_required
def projectmember_detail(request,projectmember_id):
    if request.method == 'GET':
        projectmember = get_object_or_404(ProjectMember, pk=projectmember_id, user=request.user)
        form =ProjectMemberForm(instance=projectmember)
        return render(request, 'projectmember_detail.html', {'projectmember': projectmember, 'form': form})
    else:
        try:
           projectmember = get_object_or_404(projectmember, pk=projectmember_id, user=request.user)
           form = ProjectMemberForm(request.POST, instance=projectmember)
           form.save()
           return redirect('projectmembers')
        except ValueError:
            return render(request, 'projectmember_detail.html',
                           {'projectmember': projectmember, 'form': form, 'error': 'Error updating projectmember.'})

@login_required
def complete_projectmember(request, projectmember_id):
    projectmember = get_object_or_404(projectmember, pk=projectmember_id, user=request.user)
    if request.method == 'POST':
        projectmember.datecompleted = timezone.now()
        projectmember.save()
        return redirect('projectmembers')

@login_required
def delete_projectmember(request,projectmember_id):
    projectmember = get_object_or_404(ProjectMember, pk=projectmember_id, user=request.user)
    if request.method == 'POST':
       projectmember.delete()
       return redirect('projectmembers')    
             
             