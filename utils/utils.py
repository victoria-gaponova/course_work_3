import json


def load_data(filename):
    """
    Открывает файл в формате JSON и возвращает стандартный питоновский объект
    :return: стандартный питоновский файл
    """
    with open(filename, 'r',encoding='utf-8')as file:
        return json.load(file)

