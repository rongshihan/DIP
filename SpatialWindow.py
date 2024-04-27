from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from SpaWindow import Ui_Dialog


class MySpaWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MySpaWindow, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.retranslateUi(self)

    def on_combobox_current_index_changed(self, index):
        self.label_2.show()
        self.label_3.show()
        self.lineEdit_1.show()
        self.lineEdit_2.show()
        if index == 1:
            self.lineEdit_1.setReadOnly(True)
        else:
            self.lineEdit_1.setReadOnly(False)

        if index == 3 or index == 4 or index == 5 or index == 6:
            self.label_2.hide()
            self.label_3.hide()
            self.lineEdit_1.hide()
            self.lineEdit_2.hide()

    def accept(self):
        # 重写accept方法，以获取输入框内容
        if self.comboBox.currentText() == '中值滤波' and self.lineEdit_1.text().strip() == '':
            # 如果选择中值滤波且lineEdit_1为空
            self.close()
        elif self.lineEdit_1.text().strip() == '' or self.lineEdit_2.text().strip() == '':
            # 如果两者之一为空
            self.close()
        else:
            # 如果不为空，则调用父类的accept方法
            super().accept()

    def reject(self):
        # 重写reject方法，以处理取消按钮点击事件
        super().reject()  # 调用基类的reject方法关闭对话框

