# Generated by Django 3.0.5 on 2020-05-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='plan',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan_slug',
            field=models.SlugField(blank=True, max_length=140, null=True),
        ),
    ]