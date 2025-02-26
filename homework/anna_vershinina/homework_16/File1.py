import csv
import os
from pathlib import Path
import dotenv
import mysql.connector as mysql


def read_csv(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        file_data = csv.DictReader(csvfile)
        data = [row for row in file_data]
        return data


def db_connect():
    dotenv.load_dotenv()
    db = mysql.connect(
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSW"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
    )
    return db


def search_db(db, data):
    select_query = '''
    SELECT name, second_name, g.title,
    b.title, s2.title, l.title, m.value
    FROM students s JOIN `groups` g
    ON s.group_id = g.id
    LEFT JOIN marks m
    ON s.id = m.student_id
    LEFT JOIN lessons l
    ON l.id = m.lesson_id
    LEFT JOIN subjets s2
    ON l.subject_id = s2.id
    LEFT JOIN books b
    ON b.taken_by_student_id = s.id
    WHERE s.name = %s
    AND s.second_name = %s
    AND g.title = %s
    AND b.title = %s
    AND s2.title = %s
    AND l.title = %s
    AND m.value = %s;
    '''

    cursor = db.cursor(dictionary=True)

    for each_dict in data:
        cursor.execute(select_query, (
            each_dict["name"],
            each_dict["second_name"],
            each_dict["group_title"],
            each_dict["book_title"],
            each_dict["subject_title"],
            each_dict["lesson_title"],
            each_dict["mark_value"]
        ))
        result = cursor.fetchall()
        if not result:
            print(f'Not found in the DB: {each_dict}')

    cursor.close()


def main():
    root_dir = Path(__file__).resolve().parent.parent.parent
    file_path = (
        root_dir / 'eugene_okulik' / 'Lesson_16' / 'hw_data' / 'data.csv'
    )

    data = read_csv(file_path)
    connection = db_connect()
    search_db(connection, data)
    connection.close()


if __name__ == "__main__":
    main()
