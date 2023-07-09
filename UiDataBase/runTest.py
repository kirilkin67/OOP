from PyQt6.QtWidgets import QMessageBox
from testForm import Ui_Dialog
from test_data_base import TestDataBase


class RunTest:
    def __init__(self, ui: Ui_Dialog(), db: TestDataBase):
        self.ui = ui
        self.db = db
        self.test_name = None
        self.tasks = tuple()
        self.count = 0
        self.num = 1
        print(f"TEST - {self.test_name}")

    def setQuestionAnswer(self, index: int):
        question_id, test_id, question = self.tasks[index]
        answers = self.db.select_answers(question_id)
        self.clearRadioButton()
        self.ui.question.setText(question)
        self.ui.response_1.setText(answers[0][2])
        self.ui.response_2.setText(answers[1][2])
        self.ui.response_3.setText(answers[2][2])

    def runTest(self, test_name):
        self.test_name = test_name
        self.db.select_test_name_id(self.test_name)
        self.tasks = self.db.select_questions()
        self.count = len(self.tasks)
        self.chooseTask()

    def chooseTask(self):
        if self.num != self.count:
            self.setQuestionAnswer(self.num)
            self.num += 1

    def nextTask(self):
        if self.ui.response_1.isChecked() or self.ui.response_2.isChecked() or self.ui.response_3.isChecked():
            self.chooseTask()
        else:
            self.show_dialog()

    @staticmethod
    def show_dialog():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Информационное сообщение")
        msg_box.setText("Необходимо выбрать вариант ответа")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()

    def clearRadioButton(self):
        self.ui.response_1.setAutoExclusive(False)
        self.ui.response_2.setAutoExclusive(False)
        self.ui.response_3.setAutoExclusive(False)
        self.ui.response_1.setChecked(False)
        self.ui.response_2.setChecked(False)
        self.ui.response_2.setChecked(False)
