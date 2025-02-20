import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# 1. Create a student.
query_insert_students = '''
INSERT INTO students (name, second_name, group_id)
VALUES (%s, %s, %s)
'''
values_student = ('Jane', 'Smith', None)
cursor.execute(query_insert_students, values_student)

# Record the student ID and print it.
student_id = cursor.lastrowid
print(f'The student with ID {student_id} was added')

# 2. Create books.
query_insert_book = '''
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
'''
values_books = [
    ('Moby Dick', student_id),
    ('Dracula', student_id)
]
cursor.executemany(query_insert_book, values_books)

# Printing which books were created.
cursor.execute("SELECT id FROM books WHERE taken_by_student_id = %s",
               (student_id,))

# Saving IDs of the created books and printing them.
books_created = cursor.fetchall()
book_1, book_2 = books_created[0]['id'], books_created[1]['id']
print(f"The books with IDs {book_1}, {book_2} were created")

# 3. Create a group.
query_insert_groups = '''
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
'''
values_group = ('Biology', 'Dec 2005', 'May 2010')
cursor.execute(query_insert_groups, values_group)

# Saving the group id and printing it.
group_id = cursor.lastrowid
print(f'The group with ID {group_id} was created')

# 4. Update the student's group with the created one.
cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)
cursor.execute("SELECT * FROM students WHERE students.id = %s",
               (student_id,))
updated_student = cursor.fetchone()
print(f'The record of the student was updated: {updated_student}')

# 5. Create new subjects.
cursor.executemany(
    "INSERT INTO subjets (title) VALUES (%s)",
    [('Molecular Biology',), ('Anatomy',), ('Histology',)]
)

cursor.execute("SELECT id FROM subjets ORDER BY id DESC LIMIT 3")
subjects_created = cursor.fetchall()

subj_1, subj_2, subj_3 = (
    subjects_created[0]['id'],
    subjects_created[1]['id'],
    subjects_created[2]['id']
)
print(f"The subjects with IDs {subj_1}, {subj_2}, {subj_3} were created")

# 6. Creating lessons for subjects
cursor.executemany(
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
    [
        ('Morning class Thursday', subj_1),
        ('Evening class Friday', subj_1),
        ('Morning class Monday', subj_2),
        ('Day class Wednesday', subj_2),
        ('Evening class Friday', subj_3),
        ('Morning class Tuesday', subj_3),
    ]
)
cursor.execute("SELECT id FROM lessons ORDER BY id DESC LIMIT 6")
lessons = cursor.fetchall()

lesson_1, lesson_2, lesson_3, lesson_4, lesson_5, lesson_6 = [
    row['id'] for row in lessons
]
print(
    f'Lessons with IDs {lesson_1}, {lesson_2}, {lesson_3}, '
    f'{lesson_4}, {lesson_5}, {lesson_6} were created'
)

# 7. Insert marks for created lessons for the student
# AND 8. Select all marks for the given student

cursor.executemany(
    '''
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
    ''',
    [
        (4.0, lesson_1, student_id),
        (3.5, lesson_2, student_id),
        (3.8, lesson_3, student_id),
        (3.9, lesson_4, student_id),
        (3.1, lesson_5, student_id),
        (3.0, lesson_6, student_id),
    ]
)

cursor.execute("SELECT value FROM marks m WHERE student_id = %s",
               (student_id,))
marks = cursor.fetchall()

print(f'Student with ID {student_id} has marks {marks}')

# 9. Select all the books that the given student has taken

cursor.execute(
    "SELECT * FROM books WHERE taken_by_student_id = %s",
    (student_id,)
)
taken_books = cursor.fetchall()
print(f'The student with id {student_id} has taken the following books: ',
      *taken_books, sep="\n")

# 10. Select all information about the student

cursor.execute('''
SELECT * FROM students s join `groups` g
ON s.group_id = g.id
JOIN books b
ON b.taken_by_student_id = s.id
JOIN marks m
ON m.student_id = s.id
JOIN lessons l
ON l.id = m.lesson_id
JOIN subjets s2
ON s2.id = l.subject_id WHERE s.id = %s
''', (student_id,))

student_info = cursor.fetchall()
print(f'All information regarding the student with ID: {student_id}: ',
      *student_info, sep="\n")

db.commit()
cursor.close()
db.close()
