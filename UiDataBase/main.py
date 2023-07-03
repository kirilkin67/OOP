from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from testForm import Ui_Dialog
import sys
from test_data_base import TestDataBase
import json

DATA_BASE = "subject_tests.db"


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
        print(f'ВОПРОС - {result}')
        data_base.insert_questions(result)
        for response in item["answers"]:
            print(f'ОТВЕТ на ВОПРОС - {response["response"]}, ПРАВДА - {response["correct"]}')
            data_base.insert_answers(result, response["response"], response["correct"])


def insert_value_in_data_base(data_base: TestDataBase, json_obj):
    data_base.insert_subject(json_obj["subject"])
    data_base.insert_test_name(json_obj["test_name"])
    insert_questions_and_answers(data_base, json_obj["questions"])


def create_test_data():
    file_json_name = "history.json"
    db = TestDataBase(DATA_BASE)
    create_data_base(db)
    test_subject = read_test_file_json(file_json_name)
    insert_value_in_data_base(db, test_subject)


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

# ui.subject.setTe

Dialog.show()
sys.exit(app.exec())
