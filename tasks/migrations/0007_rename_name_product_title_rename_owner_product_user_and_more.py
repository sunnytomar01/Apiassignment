# Generated by Django 5.0.7 on 2024-12-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_rename_title_product_name_rename_user_product_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Owner',
            new_name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='Status',
            field=models.TextField(choices=[('TO_DO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TO_DO', max_length=12),
        ),
        migrations.AddField(
            model_name='product',
            name='priority',
            field=models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='LOW', max_length=7),
        ),
    ]
