from PyQt6.QtWidgets import QMessageBox
from testForm import Ui_Dialog
from test_data_base import TestDataBase


class RunTest:
    def __init__(self, ui: Ui_Dialog(), db: TestDataBase):
        self.ui = ui
        self.db = db
        self.test_name = None
        self.tasks = tuple()
        self.question_count = 0
        self.num = 0
        self.question_id = int()
        self.answers = tuple()

    def clickerTestNameComboBox(self):
        self.ui.question.clear()
        self.ui.start.setEnabled(True)

    def clickerStart(self):
        self.activatedTestButton()
        self.test_name = self.ui.testName.currentText()
        self.db.delete_test_result()
        self.db.select_test_name_id(self.test_name)
        self.tasks = self.db.select_questions()
        self.question_count = len(self.tasks)
        self.chooseTask()

    def activatedTestButton(self):
        self.ui.question.clear()
        self.ui.subject.setEnabled(False)
        self.ui.testName.setEnabled(False)
        self.visibleResponses(True)
        self.ui.next.setEnabled(True)
        self.ui.stop.setEnabled(True)
        self.ui.start.setEnabled(False)

    def chooseTask(self):
        self.activeCheckableResponses(False)
        if self.num < self.question_count:
            self.setQuestionAnswer(self.num)
            self.ui.info.setText(f'Вопрос {self.num + 1} из {self.question_count}')
            self.num += 1
        if self.num == self.question_count:
            self.ui.next.setEnabled(False)

    def setQuestionAnswer(self, index: int):
        self.question_id, test_id, question = self.tasks[index]
        self.answers = self.db.select_answers(self.question_id)

        self.ui.question.setText(question)
        self.ui.response_1.setText(self.answers[0][2])
        self.ui.response_2.setText(self.answers[1][2])
        self.ui.response_3.setText(self.answers[2][2])
        self.activeCheckableResponses(True)

    def clickerNext(self):
        self.addAnswerResultInDataBase()
        if self.isCheckedRadioButton():
            self.chooseTask()

    def clickerStop(self):
        self.addAnswerResultInDataBase()
        if self.isCheckedRadioButton():
            self.activeCheckableResponses(False)
            self.ui.next.setEnabled(False)
            self.ui.stop.setEnabled(False)
            self.ui.question.clear()
            self.ui.question.setText(f"Ваш результат - {self.db.select_result()} балла")
            self.clearResponses()
            self.visibleResponses(False)
            self.ui.subject.setEnabled(True)
            self.ui.testName.setEnabled(True)
            self.num = 0

    def addAnswerResultInDataBase(self):
        if self.ui.response_1.isChecked():
            self.db.insert_test_result(self.question_id, self.answers[0][2], self.answers[0][3])
        elif self.ui.response_2.isChecked():
            self.db.insert_test_result(self.question_id, self.answers[1][2], self.answers[1][3])
        elif self.ui.response_3.isChecked():
            self.db.insert_test_result(self.question_id, self.answers[2][2], self.answers[2][3])
        else:
            self.show_dialog()

    @staticmethod
    def show_dialog():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Информационное сообщение")
        msg_box.setText("Необходимо выбрать вариант ответа")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()

    def activeCheckableResponses(self, isActive: bool):
        self.ui.response_1.setCheckable(isActive)
        self.ui.response_2.setCheckable(isActive)
        self.ui.response_3.setCheckable(isActive)

    def clearResponses(self):
        self.ui.response_1.setText('')
        self.ui.response_2.setText('')
        self.ui.response_3.setText('')

    def visibleResponses(self, isVisible: bool):
        self.ui.response_1.setVisible(isVisible)
        self.ui.response_2.setVisible(isVisible)
        self.ui.response_3.setVisible(isVisible)

    def isCheckedRadioButton(self):
        return self.ui.response_1.isChecked() or self.ui.response_2.isChecked() or self.ui.response_3.isChecked()
