# Generated by Django 3.1.7 on 2021-03-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_Register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
