# Generated by Django 4.1.3 on 2022-11-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0004_remove_jobs_technologies_master_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='technologies_master',
            field=models.ManyToManyField(to='companys.technology', verbose_name='tecnologias_dominadas'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='technology_study',
            field=models.ManyToManyField(related_name='estudar', to='companys.technology', verbose_name='tecnoligias_estudar'),
        ),
    ]
