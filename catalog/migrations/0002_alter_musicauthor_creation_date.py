# Generated by Django 5.0.1 on 2024-02-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicauthor',
            name='creation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
