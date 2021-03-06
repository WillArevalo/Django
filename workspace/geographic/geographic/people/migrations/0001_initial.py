# Generated by Django 2.0.1 on 2018-03-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0002_country_continent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('nacionality', models.ManyToManyField(to='countries.Country')),
            ],
        ),
    ]
