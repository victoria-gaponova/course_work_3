import json



def load_data(path):
    """
    Получает путь к JSON-файлу и возвращает список словарей
    :return: список словарей
    """
    with open(path, 'r', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def select_operations(operations):
    """
    Получает список банковских операций и возвращает список удачно проведенных операций
    :return:список успешно пройденных банковских операций
    """
    selected_operations = [operation for operation in operations if operation.get("state") == "EXECUTED"]
    return selected_operations


def _get_date(operation):
    """
    Получает данные банковской операции и возвращает только дату проведения банковской операции
    :param operation: данные банковской операции
    :return: дата проведения банковской операции
    """
    return operation["date"]


def sort_operations(selected_operations):
    """
    Получает список успешно пройденных банковских операций
    и возвращает отсортированный по дате (по убыванию) список банковских операций
    :param selected_operations: список успешно пройденных банковских операций
    :return:отсортированный по дате (по убыванию) список банковских операций
    """
    sorted_operations = sorted(selected_operations, key=_get_date, reverse=True)
    return sorted_operations


def get_five_last_operations(sorted_operations):
    """
    Получает список банковских операций и возвращает 5 последних
    :param sorted_operations: отсортированный по дате (по убыванию) список операций
    :return: 5 последних банковских операций
    """
    five_last_operations = sorted_operations[:5]
    return five_last_operations


def formate_date(data):
    """Возвращает строку даты из формата «ГГГГ-ММ-ДД» в «ДД.ММ.ГГГГ»

    :param five_last_operations: 
    :return:строка даты в формате «ДД.ММ.ГГГГ»
    """
    date = data.split("T")[0].split("-")[::-1]
    return ".".join(date)


def _formate_card(card_number):
    return f'{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}'


def _formate_account(account):
    return f"**{account[-4:]}"

def check_order(order):
    return _formate_card(order) if len(order) == 16 else _formate_account(order)

def check_from(operation):
    return operation["from"] if operation.get("from") else None

