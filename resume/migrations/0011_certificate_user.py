# Generated by Django 4.2.2 on 2023-08-01 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_remove_certificate_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='certificate', to=settings.AUTH_USER_MODEL),
        ),
    ]
