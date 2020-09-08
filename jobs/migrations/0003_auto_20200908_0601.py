# Generated by Django 3.0.3 on 2020-09-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200905_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='Job Title', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=300),
        ),
    ]