from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from testForm import Ui_Dialog
import sys
from test_data_base import TestDataBase
import json

DATA_BASE = "subject_tests.db"
TEST_NAME = "Искусство Древнего Египта"
questions = tuple()


def read_test_file_json(name: str):
    """
    Чтение файла расширением json и преобразование его в объект для записи в БД
    :param name: имя файла расширением json
    :return: объект типа json
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = file.read()
        test = json.loads(data)
        return test
    except FileNotFoundError:
        print("Файл не найден или не существует")


def create_data_base(data_base: TestDataBase):
    data_base.create_table_subject()
    data_base.create_table_test_name()
    data_base.create_table_questions()
    data_base.create_table_answers()
    return data_base


def insert_questions_and_answers(data_base: TestDataBase, items: list):
    for item in items:
        result = item["question"]
        data_base.insert_questions(result)
        for response in item["answers"]:
            data_base.insert_answers(result, response["response"], response["correct"])


def insert_value_in_data_base(data_base: TestDataBase, json_obj):
    data_base.insert_subject(json_obj["subject"])
    data_base.insert_test_name(json_obj["test_name"])
    insert_questions_and_answers(data_base, json_obj["questions"])


def add_test(file_name_json: str):
    test_subject = read_test_file_json(file_name_json)
    insert_value_in_data_base(db, test_subject)


def setQuestionAnswer(tasks: tuple, index: int):
    question_id, test_id, question = tasks[index]
    answers = db.select_answers(question_id)
    ui.question.setText(question)
    ui.response_1.setText(answers[0][2])
    ui.response_2.setText(answers[1][2])
    ui.response_3.setText(answers[2][2])


def setSubjectComboBox():
    rows = db.select_subject_name_all()
    ui.subject.addItem("Выбор предмета")
    for row in rows:
        subject_id, subject = row
        ui.subject.addItem(subject)


def setTestNameComboBox():
    rows = db.select_test_name()
    ui.testName.addItem("Выбор теста")
    for row in rows:
        ui.testName.addItem(row[0])


def clearAll():
    ui.testName.clear()
    ui.question.clear()
    ui.response_1.setText('')
    ui.response_2.setText('')
    ui.response_3.setText('')


def clickerSubjectComboBox():
    clearAll()
    subject_name = ui.subject.currentText()
    print(f"ПРЕДМЕТ - {subject_name}")
    db.select_subject_id_by_name(subject_name)
    setTestNameComboBox()


def clickerTestNameComboBox():
    ui.question.clear()
    test_name = ui.testName.currentText()
    print(f"TEST - {test_name}")
    db.select_test_name_id(test_name)
    tasks = db.select_questions()
    setQuestionAnswer(tasks, 1)


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)


db = TestDataBase(DATA_BASE)
create_data_base(db)
history = "history.json"
add_test(history)
history = "history2.json"
add_test(history)

setSubjectComboBox()
ui.subject.activated.connect(clickerSubjectComboBox)
ui.testName.activated.connect(clickerTestNameComboBox)


Dialog.show()
sys.exit(app.exec())
