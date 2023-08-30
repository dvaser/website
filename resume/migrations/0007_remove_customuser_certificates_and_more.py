# Generated by Django 4.2.2 on 2023-07-31 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_remove_certificate_user_remove_education_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='certificates',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='educations',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='experiencies',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='links',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='projects',
        ),
        migrations.AddField(
            model_name='certificate',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='certificate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='education', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experience', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='link',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
