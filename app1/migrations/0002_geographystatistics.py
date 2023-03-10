# Generated by Django 4.1.5 on 2023-01-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeographyStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph', models.ImageField(upload_to='img/', verbose_name='Графики')),
                ('table_first', models.TextField(verbose_name='Таблица с зарплатами')),
                ('table_second', models.TextField(verbose_name='Таблица с вакансиями')),
            ],
            options={
                'verbose_name': 'Статистика географии',
                'verbose_name_plural': 'Статистики географии',
            },
        ),
    ]
