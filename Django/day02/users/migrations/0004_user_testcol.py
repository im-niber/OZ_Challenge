# Generated by Django 5.0.6 on 2024-05-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='testcol',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
