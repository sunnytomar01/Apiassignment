from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Projects'

class ProjectMemberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projectmember'

class CommentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comment'