# Generated by Django 5.0.3 on 2024-06-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riderprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='username', max_length=200),
            preserve_default=False,
        ),
    ]
