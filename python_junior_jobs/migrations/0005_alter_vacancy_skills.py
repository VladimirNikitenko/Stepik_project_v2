# Generated by Django 4.0.3 on 2022-03-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_junior_jobs', '0004_alter_vacancy_salary_max_alter_vacancy_salary_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=250),
        ),
    ]
