# Generated by Django 4.0.3 on 2022-03-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_junior_jobs', '0006_alter_vacancy_salary_max_alter_vacancy_salary_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.IntegerField(),
        ),
    ]