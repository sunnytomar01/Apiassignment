# Generated by Django 5.0.7 on 2024-12-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_datecompleted_alter_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='important',
        ),
        migrations.AddField(
            model_name='task',
            name='Status',
            field=models.TextField(choices=[('TO_DO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TO_DO', max_length=12),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='LOW', max_length=7),
        ),
    ]