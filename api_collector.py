import requests
import pandas as pd
import json


class ApiCollector:
    @staticmethod
    def parse_response():
        def get(dict, key):
            try:
                return dict.get(key)
            except:
                return None

        result_array = []
        for page in range(19):
            params = {
                'specialization': 1,
                'text': 'NAME:C#',
                'page': page,
                'per_page': 100,
                'only_with_salary': True,
                'date_from': f'2022-12-27T00:00:00',
                'date_to': f'2022-12-27T23:59:59'
            }
            res = requests.get(f'https://api.hh.ru/vacancies', params)
            if res.status_code == 200:
                parsedJson = json.loads(res.text)["items"]
                result_array.append(pd.DataFrame([{'name': get(item, 'name'),
                                                   'salary_from': get(get(item, 'salary'), 'from'),
                                                   'salary_to': get(get(item, 'salary'), 'to'),
                                                   'salary_currency': get(get(item, 'salary'), 'currency'),
                                                   'salary_gross': get(get(item, 'salary'), 'gross'),
                                                   'area_name': get(get(item, 'area'), 'name'),
                                                   'published_at': get(item, 'published_at')} for item in parsedJson]))

        return pd.concat(result_array, ignore_index=True)

