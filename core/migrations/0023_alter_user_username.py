# Generated by Django 5.0.3 on 2024-07-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_order_delivery_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=90),
        ),
    ]