from django.db import models


class DemandStatistics(models.Model):
    graph = models.ImageField('Графики', upload_to='img/')
    tables = models.TextField('Таблицы')

    class Meta:
        verbose_name = 'Статистика востребованности'
        verbose_name_plural = 'Статистики востребованности'


class GeographyStatistics(models.Model):
    graph = models.ImageField('Графики', upload_to='img/')
    table_first = models.TextField('Таблица с зарплатами')
    table_second = models.TextField('Таблица с вакансиями')

    class Meta:
        verbose_name = 'Статистика географии'
        verbose_name_plural = 'Статистики географии'


class SkillsStatistics(models.Model):
    graph_1 = models.ImageField('График', upload_to='img/')
    graph_2 = models.ImageField('График', upload_to='img/')
    graph_3 = models.ImageField('График', upload_to='img/')
    graph_4 = models.ImageField('График', upload_to='img/')
    graph_5 = models.ImageField('График', upload_to='img/')
    graph_6 = models.ImageField('График', upload_to='img/')
    graph_7 = models.ImageField('График', upload_to='img/')

    class Meta:
        verbose_name = 'Статистика навыков'
        verbose_name_plural = 'Статистики навыков'
