from src.utils import load_data, select_operations, sort_operations, get_five_last_operations, formate_date, \
   check_order, check_from


def test_load_data(file):
    assert load_data(file)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_select_operations(data):
    assert select_operations(data) == [data[0]]


def test_sort_operations(data):
    assert sort_operations(data) == [data[0], data[1]]


def test_get_five_last_operations():
    assert get_five_last_operations([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5]


def test_formate_date():
    assert formate_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_check_order():
    assert check_order("14211924144426031657") == "**1657"
    assert check_order("1246377376343588") == "1246 37** **** 3588"

def test_check_from():
    assert check_from({"from": "jdsf"}) == "jdsf"
    assert check_from({"fr": "jdsf"}) == None