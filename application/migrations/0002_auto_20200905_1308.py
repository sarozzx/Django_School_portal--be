# Generated by Django 3.1 on 2020-09-05 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='application.assignment'),
        ),
    ]
