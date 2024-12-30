"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('projects/', views.projects, name='projects'),
    path('projects_completed/', views.projects_completed, name='projects_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_project/', views.create_project, name='create_project'),
    path('projects/<int:project_id>', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/complete', views.complete_project, name='complete_project'),
    path('projects/<int:project_id>/delete', views.delete_project, name='delete_project'),

    
    path('create_comment/', views.create_comment, name='create_comment'),
    path('comments/<int:comment_id>', views.comment_detail, name='comment_detail'),
    path('comments/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path('comments/', views.comments, name='comments'),
    path('comments_completed/', views.comments_completed, name='comments_completed'),
    path('comments/<int:comment_id>/complete', views.complete_comment, name='complete_comment'),

    path('create_projectmember/', views.create_projectmember, name='create_projectmember'),
    path('projectmembers/<int:projectmember_id>', views.projectmember_detail, name='projectmember_detail'),
    path('projectmembers/<int:projectmember_id>/delete', views.delete_projectmember, name='delete_projectmember'),
    path('projectmembers/', views.projectmembers, name='projectmembers'),
    path('projectmembers_completed/', views.projectmembers_completed, name='projectmembers_completed'),
    path('projectmembers/<int:projectmember_id>/complete', views.complete_projectmember, name='complete_projectmember'),
]