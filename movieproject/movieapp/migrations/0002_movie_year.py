# Generated by Django 3.2.15 on 2022-09-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
