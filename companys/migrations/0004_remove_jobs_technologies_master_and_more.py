# Generated by Django 4.1.3 on 2022-11-11 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0003_jobs_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='technologies_master',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='technology_study',
        ),
    ]