# Generated by Django 5.0.6 on 2024-06-03 10:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
        ('reviews', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.CharField(default='not', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='feed',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='feeds.feed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='likes_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
