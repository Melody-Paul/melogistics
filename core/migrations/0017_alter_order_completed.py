# Generated by Django 5.0.3 on 2024-07-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_order_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]