# Generated by Django 4.1.2 on 2023-01-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
            ],
        ),
    ]