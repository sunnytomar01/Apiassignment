from django.contrib import admin
from .models import Task , Project , ProjectMember ,Comment

class TaskAdmin (admin.ModelAdmin):
    readonly_fields = ("created", )
admin.site.register(Task, TaskAdmin)

class ProjectAdmin (admin.ModelAdmin):
    readonly_fields = ("created", )
admin.site.register(Project, ProjectAdmin)

class CommentAdmin (admin.ModelAdmin):
    readonly_fields = ("created", )
admin.site.register(Comment, CommentAdmin)

class ProjectMemberAdmin (admin.ModelAdmin):
    readonly_fields = ("created", )
admin.site.register(ProjectMember, ProjectMemberAdmin)