# Generated by Django 2.0.5 on 2018-05-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'permissions': (('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin'))},
        ),
        migrations.AddField(
            model_name='member',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
    ]
