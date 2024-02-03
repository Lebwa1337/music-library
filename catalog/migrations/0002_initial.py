# Generated by Django 5.0.1 on 2024-02-03 13:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='track',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ManyToManyField(to='catalog.genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='tracks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.track'),
        ),
    ]
