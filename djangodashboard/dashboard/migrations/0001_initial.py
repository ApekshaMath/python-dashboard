# Generated by Django 3.2.7 on 2023-06-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header1', models.CharField(max_length=250)),
                ('header2', models.CharField(max_length=250)),
                ('header3', models.CharField(max_length=250)),
                ('header4', models.CharField(max_length=250)),
                ('header5', models.CharField(max_length=250)),
                ('header6', models.CharField(max_length=250)),
            ],
        ),
    ]