# Generated by Django 4.1.3 on 2022-11-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='Technology_study',
            new_name='technology_study',
        ),
    ]
