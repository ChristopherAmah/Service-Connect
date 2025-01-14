# Generated by Django 5.0.3 on 2024-03-12 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceconnectapp', '0007_delete_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='automobile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='beauty',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceconnectapp.category'),
        ),
        migrations.AddField(
            model_name='service',
            name='catering',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='domestic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='events',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='hair',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='more',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='tech',
            field=models.BooleanField(default=False),
        ),
    ]
