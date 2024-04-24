from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from CLAHEWindow import Ui_Dialog


class MyCLAHEWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MyCLAHEWindow, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.retranslateUi(self)

    def accept(self):
        text1 = self.lineEdit_1.text().strip()
        text2 = self.lineEdit_2.text().strip()
        text3 = self.lineEdit_3.text().strip()
        if text1 == '' or text2 == '' or text3 == '':
            # 如果三者之一为空
            self.close()
        else:
            # 如果三者都不为不为空，则调用父类的accept方法
            super().accept()

    def reject(self):
        super().reject()
