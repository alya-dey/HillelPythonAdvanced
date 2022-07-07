from flask import Flask
from utils import read_requirements, generate_users, get_number_of_astros, avr_from_csv

app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    result = read_requirements()
    return result


@app.route('/generate-users/')
def users():
    # <br>
    users_list = generate_users(100)
    return str(users_list)


@app.route('/space/')
def space():
    number_of_astros = get_number_of_astros()
    return number_of_astros


@app.route('/mean/')
def mean():
    avr_data = avr_from_csv()
    return avr_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


'''
1. Возвращать содержимое файла с пайтон пакетами (requirements.txt)
PATH: /requirements/ открыть файл requirements.txt и вернуть его содержимое

2. Вывести 100 случайно сгенерированных юзеров (почта + имя) 'Dmytro aasdasda@mail.com'
PATH: /generate-users/ ( https://pypi.org/project/Faker/ )
+ параметр который регулирует количество юзеров

3. Вывести количество космонавтов в настоящий момент (http://api.open-notify.org/astros.json) (https://pypi.org/project/requests/)
PATH: /space/
 import requests
 r = requests.get('https://api.github.com/repos/psf/requests')
 r.json()["description"]

* Считать файл hw.csv и посчитать средний рост, средний вес в см и кг соответственно
PATH: /mean/

!!! прислать 3 файла main.py, utils.py, requirements.txt !!!
'''
