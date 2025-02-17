import os
import datetime


def convert_to_date(line):
    date_converted = datetime.datetime.strptime(
        line[3:29], "%Y-%m-%d %H:%M:%S.%f"
    )
    return date_converted


def read_file(file):
    with open(file, 'r') as data_file:
        line_count = 0
        for line in data_file:
            line_count += 1
            if line_count == 1:
                date_1 = convert_to_date(line)
                print(date_1 + datetime.timedelta(days=7))
            elif line_count == 2:
                date_2 = convert_to_date(line).date()
                print(f'The date "{date_2}" is '
                      f'{date_2.weekday()}th day of the week')
            elif line_count == 3:
                date_3 = convert_to_date(line).date()
                date_now = datetime.datetime.today().date()
                print(f'The date "{date_3}" was '
                      f'{(date_now - date_3).days} days ago')


repo_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
file_path = os.path.join(repo_root, "eugene_okulik", "hw_13", "data.txt")
read_file(file_path)
