# Generated by Django 5.0.6 on 2024-05-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozusers', '0002_rename_users_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
