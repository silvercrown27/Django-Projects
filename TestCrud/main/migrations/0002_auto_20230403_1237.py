# Generated by Django 3.2.12 on 2023-04-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='message',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]