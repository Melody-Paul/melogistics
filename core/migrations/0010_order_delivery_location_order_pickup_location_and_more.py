# Generated by Django 5.0.3 on 2024-06-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_oder_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_location',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_location',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riderprofile',
            name='busy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='riderprofile',
            name='total_star',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]
