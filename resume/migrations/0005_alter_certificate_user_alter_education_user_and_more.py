# Generated by Django 4.2.2 on 2023-07-28 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_certificate_user_alter_education_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='certificate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='education', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experience', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='link',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
