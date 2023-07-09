from PyQt6 import QtWidgets
from testForm import Ui_Dialog
from PyQt6.QtWidgets import QMessageBox
import sys
from test_data_base import TestDataBase
from runTest import RunTest
import json

DATA_BASE = "subject_tests.db"
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
        test_data = json.loads(data)
        return test_data
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


# def setQuestionAnswer(tasks: tuple, index: int):
#     question_id, test_id, question = tasks[index]
#     answers = db.select_answers(question_id)
#     ui.question.setText(question)
#     ui.response_1.setText(answers[0][2])
#     ui.response_2.setText(answers[1][2])
#     ui.response_3.setText(answers[2][2])
#

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
    ui.start.setEnabled(False)


def clearResponses():
    ui.response_1.setText('')
    ui.response_2.setText('')
    ui.response_3.setText('')


def activeResponses(isActive: bool):
    ui.response_1.setEnabled(isActive)
    ui.response_2.setEnabled(isActive)
    ui.response_3.setEnabled(isActive)


def clickerSubjectComboBox():
    clearAll()
    subject_name = ui.subject.currentText()
    print(f"ПРЕДМЕТ - {subject_name}")
    db.select_subject_id_by_name(subject_name)
    setTestNameComboBox()


def clickerTestNameComboBox():
    ui.question.clear()
    clearResponses()
    ui.start.setEnabled(True)


def clickerStart():
    ui.question.clear()
    activatedTestButton()
    test_name = ui.testName.currentText()
    test.runTest(test_name)


def activatedTestButton():
    ui.subject.setEnabled(False)
    ui.testName.setEnabled(False)
    activeResponses(True)
    ui.next.setEnabled(True)
    ui.stop.setEnabled(True)
    ui.start.setEnabled(False)


def mainWindow():
    ui.start.setEnabled(False)
    activeResponses(False)
    ui.next.setEnabled(False)
    ui.stop.setEnabled(False)


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

db = TestDataBase(DATA_BASE)
test = RunTest(ui, db)

# create_data_base(db)
# history = "history.json"
# add_test(history)
# history = "history2.json"
# add_test(history)

# ui.start.setVisible(False)
mainWindow()
setSubjectComboBox()
ui.subject.activated.connect(clickerSubjectComboBox)
ui.testName.activated.connect(clickerTestNameComboBox)
ui.start.clicked.connect(clickerStart)
ui.next.clicked.connect(test.nextTask)


Dialog.show()
sys.exit(app.exec())
