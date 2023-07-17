# Generated by Django 4.1.7 on 2023-05-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('section', models.CharField(max_length=200)),
                ('roll_no', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=220, null=True, verbose_name='Gender')),
            ],
        ),
    ]