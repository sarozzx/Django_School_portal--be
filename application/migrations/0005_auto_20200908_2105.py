# Generated by Django 3.1 on 2020-09-08 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_remove_assignment_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='application.choice'),
        ),
        migrations.AlterField(
            model_name='question',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='application.assignment'),
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
    ]
