INSERT INTO students (name, second_name, group_id)
VALUES ('Jane', 'Smith', 129);  # 4363

INSERT INTO books (title, taken_by_student_id)
VALUES ('Mobby Dick', 4363), ('Dracula', 4363);

INSERT INTO `groups` (title, start_date, end_date)
VALUES ('Biology', 'Dec 2005', 'May 2010'); # 2753

UPDATE students SET group_id = 2753 WHERE id = 4363;

INSERT INTO subjets (title)
VALUES ('Molecular Biology'),
('Anatomy'),
('Gistology');  # 4424-26

INSERT INTO lessons (title, subject_id)
VALUES ('Morning class Thursday', 4424),
('Evening class Friday', 4424),
('Morning class Monday', 4425),
('Day class Wednesday', 4425),
('Evening class Friday', 4426),
('Morning class Tuesday', 4426)  # 8224-29

INSERT INTO marks (value, lesson_id, student_id)
VALUES (4.0, 8224, 4363),
(3.5, 8225, 4363),
(3.8, 8226, 4363),
(3.9, 8227, 4363),
(3.1, 8228, 4363),
(3.0, 8229, 4363);

SELECT * FROM marks m WHERE student_id = 4363;

SELECT * FROM books b WHERE taken_by_student_id = 4363;

SELECT * FROM students s join `groups` g
ON s.group_id = g.id
join books b
ON b.taken_by_student_id = s.id
JOIN marks m
ON m.student_id = s.id
JOIN lessons l
ON l.id = m.lesson_id
JOIN subjets s2
ON s2.id = l.subject_id WHERE s.id = 4363;



