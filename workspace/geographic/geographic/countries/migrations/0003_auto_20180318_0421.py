# Generated by Django 2.0.1 on 2018-03-18 04:21

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_country_continent'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='country',
            managers=[
                ('active_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]