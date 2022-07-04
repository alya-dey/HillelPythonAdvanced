from faker import Faker
import requests
import pandas as pd


def read_requirements() -> str:
    """
    reads requirements from requirements.txt
    """
    with open('requirements.txt') as file:
        return file.read()


def generate_users(number) -> str:
    """
    generates users
    """
    faker = Faker()
    list_of_users = []
    for i in range(number):
        list_of_users.append(f'name: {faker.name()}, email: {faker.email()}')
    return str(list_of_users)


def get_number_of_astros() -> str:
    """
    gets number of astronauts today
    """
    space_data = requests.get('http://api.open-notify.org/astros.json')
    number_of_astros = str(space_data.json()["number"])
    return number_of_astros


def avr_from_csv() -> str:
    """
    gets data from csv file with weight and height in inches and pounds, count average and turn into cm and kg
    """
    data = pd.read_csv('hw.csv')
    # cols_list = list(data)
    avr_height_inches = data[' "Height(Inches)"'].mean()
    avr_height_cm = round(avr_height_inches * 2.54)
    avr_weight_pounds = data[' "Weight(Pounds)"'].mean()
    avr_weight_kg = round(avr_weight_pounds * 0.45359237)
    return f'Average height is {avr_height_cm} cm, average weight is {avr_weight_kg} kg'
