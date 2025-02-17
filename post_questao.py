import json
import requests
import os

path = os.getcwd()


def send(year):
    folder = os.listdir(path + '/' + year)

    for json_path in folder:
        if json_path == 'images':
            continue

        with open(year + '/' + json_path) as json_file:
            questao = json.load(json_file)
            questao_json = {
                'numero': int(questao["Numero"]),
                'ano': int(questao['Ano']),
                'area': questao['Componente'],
                'subarea': questao['Subarea'],
                'resposta': int(questao['Resposta']),
                'alternativas': questao['Alternativas'],
                'enunciado': questao['Enunciado'],
                'imagens': {'enunciado': questao['Imagens'], 'alternativa_a': [], 'alternativa_b': [],
                            'alternativa_c': [], 'alternativa_d': [], 'alternativa_e': []},
                'explicacao': {'String': questao.get('Explicacao', ''), 'Valid': True}
            }

            r = requests.post(
                'http://localhost:8060/questao/', json=questao_json)
            if r.status_code == 201:
                print('year: ' + year + ', json_path: ' + json_path)
            else:
                print('year: ' + year + ', json_path: ' + json_path, r.content)


send('2016')
send('2017')
send('2018')
send('2019')
send('2022')
send('2023')