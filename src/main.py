from config import PATH_TO_OPERATIONS
from utils import load_data, select_operations, sort_operations, get_five_last_operations, formate_date, \
    check_order, check_from


def main():
    operations = load_data(PATH_TO_OPERATIONS)
    selected_operations = select_operations(operations)
    sorted_operations = sort_operations(selected_operations)
    five_last_operations = get_five_last_operations(sorted_operations)

    for operation in five_last_operations:
        date = formate_date(operation["date"])
        from_operation = check_from(operation)
        to_operation = operation["to"].split()
        print(f"{date} {operation['description']}")
        if from_operation is not None:
            from_name_order = ' '.join(from_operation.split()[:-1])
            from_number_order = check_order(from_operation.split()[-1])
            print(f"{from_name_order} {from_number_order} -> ", end="")
        print(f"{' '.join(to_operation[:-1])} {check_order(to_operation[-1])}")
        print(f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')


if __name__ == '__main__':
    main()
