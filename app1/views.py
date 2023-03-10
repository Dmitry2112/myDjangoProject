from django.shortcuts import render
from api_collector import ApiCollector
from app1.models import DemandStatistics, GeographyStatistics, SkillsStatistics


def index(request):
    data = {
        'introduction': ['''IT-сфера постоянно расширяется и требует новых профессиональных кадров. В C#-разработчиках на данный момент
        нуждаются даже крупные компании, готовые предоставить рабочее место в том числе и Junior-программистам на
        постоянной или проектной основе. Опытный разработчик на C# – настоящая находка для работодателей, а
        востребованность таких профессионалов очевидна.''',
                         '''C#-разработчик – программист, специализирующийся на веб-приложениях, декстопных и кроссплатформенных программных
        продуктах, играх, облачных сервисах. Язык C# входит в топ-5 самых востребованных языков программирования,
        а специалисты по C# необходимы даже в крупных IT-компаниях. Базовые функции C#-разработчика: Бэкенд-разработка,
        Создание высоконагруженных сайтов, Проектирование декстоп-приложения, Асинхронное программирование, 
        Мобильная разработка'''],

        'main_text': ['''С# считается одним из самых простых, но в то же время и самых мощных языков программирования.
        Профессия является постоянно развивающейся в связи с поддержкой языка от Microsoft.
        Многие крупные IT-компании предпочитают именно этот язык в своих разработках.
        C#-разработчик – востребованная профессия в сфере информационных технологий.
        Рост вакансий на рынке кадров составил 170% за последние два года.
        Стать C#-программистом сейчас можно с нуля практически самостоятельно, пройдя курсы по направлению
        в онлайн-школах, и начать зарабатывать уже во время обучения.''',
                      '''За последние полгода заработная плата C#-разработчиков увеличилась на 16% - это самый быстрый рост в сфере IT.
        Большая часть работодателей предпочитает нанимать программистов на удаленную работу,
        что позволяет нанимать профессионалов с любой точки мира.
        В связи с этим заработная плата часто выражается в USD.'''],

        'conclusion': '''C#-программист – постоянно развивающаяся профессия, находящаяся в топе IT-сферы.
        Окупать обучение на курсах можно начать уже во время обучения, зарекомендовав себя в крупных компаниях.
        В связи с высокой востребованностью кадров разработчик на C# никогда не останется без работы.
        Возможность программировать удаленно не привязывает к офису и позволяет вписывать работу в повседневность.'''
    }
    return render(request, 'app1/index.html', context=data)


def demand(request):
    data = {
        'demand_statistics': DemandStatistics.objects.get(id=1)
    }
    return render(request, 'app1/demand.html', context=data)


def geography(request):
    data = {
        'geography_statistics': GeographyStatistics.objects.get(id=1)
    }
    return render(request, 'app1/geography.html', context=data)


def skills(request):
    data = {
        'skills_statistics': SkillsStatistics.objects.get(id=1)
    }
    return render(request, 'app1/skills.html', context=data)


def latest_vacancies(request):
    df = ApiCollector.parse_response()
    data = {
        'df': df.to_html()
    }
    return render(request, 'app1/latest-vacancies.html', context=data)

