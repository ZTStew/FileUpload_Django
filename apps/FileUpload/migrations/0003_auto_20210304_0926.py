# Generated by Django 3.1.7 on 2021-03-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileUpload', '0002_auto_20210304_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='apps/FileUpload/documents/'),
        ),
    ]
