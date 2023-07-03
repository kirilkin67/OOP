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
                        question TEXT NOT NULL);""")
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

    def insert_subject(self, subject_name: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("INSERT OR IGNORE INTO subject (subject_name) VALUES (?)", [subject_name])
            conn.commit()
            res = cur.execute("SELECT id FROM subject WHERE subject_name = ?", [subject_name])
            self.subject_id = res.fetchone()[0]
            print(f"{subject_name}, {self.subject_id}")

    def insert_test_name(self, test_name: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            data = [self.subject_id, test_name]
            print(f"SUBJECT_ID - {self.subject_id}")
            cur.execute("INSERT OR IGNORE INTO test_name (subject_id, test_name) VALUES (?, ?)", data)
            conn.commit()
            res = cur.execute("SELECT id FROM test_name WHERE test_name = ?", [test_name])
            self.test_name_id = res.fetchone()[0]
            print(f"{test_name} - {self.test_name_id}")

    def insert_questions(self, question: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO questions (test_name_id, question) VALUES (?, ?)", [self.test_name_id, question])
            conn.commit()
            # self.test_name_id = cur.execute("SELECT id FROM test_name WHERE test_name = ?", [test_name])
            # print(f"{test_name} - {self.test_name_id}")

    def insert_answers(self, question: str, response: str, correct: bool):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            question_id = self.select_question_id(question)
            data = [question_id, response, correct]
            cur.execute("INSERT INTO answers (question_id, response, correct) VALUES (?, ?, ?)", data)
            conn.commit()

    def select_question_id(self, question: str):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT id FROM questions WHERE question = ?", [question])
            question_id, = res.fetchone()
            conn.commit()
            print(f"ID вопроса - {question_id}")
            return question_id
