from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from NoiWindow import Ui_Dialog


class MyNoiWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MyNoiWindow, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.retranslateUi(self)

        self.lineEdit_1.show()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()

    def on_combobox_current_index_changed(self, index):
        # 根据选中的索引显示或隐藏 LineEdit
        if index == 0:
            self.lineEdit_1.show()
            self.lineEdit_2.hide()
            self.lineEdit_3.hide()
        elif index == 1:
            self.lineEdit_1.hide()
            self.lineEdit_2.show()
            self.lineEdit_3.show()

    def accept(self):
        text1 = self.lineEdit_1.text().strip()
        text2 = self.lineEdit_2.text().strip()
        text3 = self.lineEdit_3.text().strip()
        combox_text = self.comboBox.currentText()
        if combox_text == '椒盐噪声' and text1 == '':
            # 如果选择椒盐噪声且lineEdit_1为空
            self.close()
        elif combox_text == '高斯噪声' and (text2 == '' or text3 == ''):
            # 如果选择高斯噪声且lineEdit_2为空或lineEdit_3为空
            self.close()
        else:
            # 如果LineEdit不为空，则调用父类的accept方法
            super().accept()

    def reject(self):
        super().reject()
