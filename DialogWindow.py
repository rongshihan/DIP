from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from DiagWindow import Ui_Dialog


class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.retranslateUi(self)

    def accept(self):
        if self.lineEdit.text().strip() == '' or self.lineEdit_2.text().strip() == '':
            # 如果LineEdit或lineEdit_2为空，则直接关闭对话框
            self.close()
        else:
            # 如果LineEdit不为空，则调用父类的accept方法
            super().accept()

    def reject(self):
        super().reject()
