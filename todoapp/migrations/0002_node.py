# Generated by Django 3.0.7 on 2020-09-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
    ]
