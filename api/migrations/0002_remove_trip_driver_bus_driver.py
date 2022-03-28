# Generated by Django 4.0.3 on 2022-03-28 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='driver',
        ),
        migrations.AddField(
            model_name='bus',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.driver'),
        ),
    ]
