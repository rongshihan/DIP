from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from SpaWindow import Ui_Dialog


class MySpaWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MySpaWindow, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.retranslateUi(self)

    def accept(self):
        # 重写accept方法，以获取输入框内容
        super().accept()  # 调用基类的accept方法关闭对话框

    def reject(self):
        # 重写reject方法，以处理取消按钮点击事件
        super().reject()  # 调用基类的reject方法关闭对话框

