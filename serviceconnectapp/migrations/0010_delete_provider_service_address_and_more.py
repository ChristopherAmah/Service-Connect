# Generated by Django 5.0.3 on 2024-03-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceconnectapp', '0009_remove_service_providers_service_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Provider',
        ),
        migrations.AddField(
            model_name='service',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='certifications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='provider_logos'),
        ),
        migrations.AddField(
            model_name='service',
            name='opening_hours',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='payment_methods',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='service',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='social_media_links',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='tags',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='service',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, default='pix.png', null=True, upload_to='providers'),
        ),
    ]
