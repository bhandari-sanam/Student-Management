# Generated by Django 4.1.7 on 2023-05-28 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll_no',
        ),
    ]
