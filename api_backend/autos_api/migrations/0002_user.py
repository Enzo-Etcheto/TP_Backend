# Generated by Django 5.0.3 on 2024-06-17 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('auto', models.ManyToManyField(blank=True, to='autos_api.autos')),
            ],
        ),
    ]
