# Generated by Django 5.0.3 on 2024-06-17 22:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_riderprofile_username_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateField(max_length=10)),
                ('stars', models.IntegerField(default=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_rides', to='core.customerprofile')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_rides', to='core.riderprofile')),
            ],
        ),
    ]
