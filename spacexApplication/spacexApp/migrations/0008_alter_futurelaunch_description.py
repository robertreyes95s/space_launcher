# Generated by Django 3.2.8 on 2022-02-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacexApp', '0007_rename_launch_site_futurelaunch_launch_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futurelaunch',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
