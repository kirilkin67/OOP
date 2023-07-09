import sqlite3


class TestDataBase:
    def __init__(self, name: str):
        self.name = name
        self.subject_id = None
        self.test_name_id = None

    def create_table_subject(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS subject (
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        subject_name TEXT NOT NULL UNIQUE);""")
            conn.commit()

    def create_table_test_name(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS test_name (
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        subject_id INTEGER NOT NULL REFERENCES subject(id),
                        test_name TEXT NOT NULL UNIQUE);""")
            conn.commit()

    def create_table_questions(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS questions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        test_name_id INTEGER NOT NULL REFERENCES test_name(id),
                        question TEXT NOT NULL UNIQUE);""")
            conn.commit()

    def create_table_answers(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS answers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question_id INTEGER NOT NULL REFERENCES questions(id), 
                        response TEXT NOT NULL, 
                        correct BOOLEAN DEFAULT FALSE);""")
            conn.commit()

    def create_table_test_result(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS test_result (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question_id INTEGER NOT NULL REFERENCES questions(id), 
                        response TEXT NOT NULL, 
                        correct BOOLEAN DEFAULT FALSE);""")
            conn.commit()

    def insert_subject(self, subject_name: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT id FROM subject WHERE subject_name = ?", [subject_name])
            row = res.fetchone()
            if row is not None:
                self.subject_id = row[0]
            else:
                cur.execute("INSERT OR IGNORE INTO subject (subject_name) VALUES (?)", [subject_name])
                conn.commit()
                res = cur.execute("SELECT id FROM subject WHERE subject_name = ?", [subject_name])
                self.subject_id = res.fetchone()[0]

    def insert_test_name(self, test_name: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            data = [self.subject_id, test_name]
            row = cur.execute("INSERT OR IGNORE INTO test_name (subject_id, test_name) VALUES (?, ?)", data)
            conn.commit()
            self.select_test_id_by_name(cur, test_name)
            return row.fetchone()

    def insert_answers(self, question: str, response: str, correct: bool):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            question_id = self.select_question_id(question)
            data = [question_id, response, correct]
            cur.execute("INSERT INTO answers (question_id, response, correct) VALUES (?, ?, ?)", data)
            conn.commit()

    def insert_questions(self, question: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO questions (test_name_id, question) VALUES (?, ?)", [self.test_name_id, question])
            conn.commit()

    def insert_test_result(self, question_id: int, response: str, correct: bool):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO test_result (question_id, response, correct) VALUES (?, ?, ?)",
                        [question_id, response, correct])
            conn.commit()

    def select_question_id(self, question: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT id FROM questions WHERE question = ?", [question])
            question_id, = res.fetchone()
            return question_id

    def select_test_name_id(self, name: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            self.select_test_id_by_name(cur, name)

    def select_test_id_by_name(self, cursor, test_name):
        res = cursor.execute("SELECT id FROM test_name WHERE test_name = ?", [test_name])
        self.test_name_id = res.fetchone()[0]

    def select_questions(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT * FROM questions WHERE test_name_id = ?", [self.test_name_id])
            return res.fetchall()

    def select_answers(self, question_id: int):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT * FROM answers WHERE question_id = ?", [question_id])
            return res.fetchall()

    def select_subject_name_all(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT * FROM subject")
            return res.fetchall()

    def select_subject_id_by_name(self, subject_name):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT id FROM subject WHERE subject_name = ?", [subject_name])
            self.subject_id = res.fetchone()[0]

    def select_test_name(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT test_name FROM test_name WHERE subject_id = ?", [self.subject_id])
            return res.fetchall()

    def select_result(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT COUNT() FROM test_result WHERE correct = true")
            return res.fetchone()[0]

    def delete_test_result(self):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM test_result")
            conn.commit()
