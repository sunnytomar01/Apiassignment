# Generated by Django 5.0.7 on 2024-12-29 21:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_rename_title_product_name_remove_product_status_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.TextField(choices=[('ADMIN', 'ADMIN'), ('MEMBER', 'MEMBER')], default='MEMBER', max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
