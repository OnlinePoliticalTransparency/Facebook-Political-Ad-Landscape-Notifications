# Generated by Django 2.2.14 on 2020-07-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organisation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
