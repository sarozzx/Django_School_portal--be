# Generated by Django 3.1 on 2020-09-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20200905_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='course',
            field=models.CharField(choices=[('maths', 'Maths'), ('english', 'English'), ('science', 'Science')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
