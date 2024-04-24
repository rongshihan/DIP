import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QMenu, QPushButton
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QListWidget with Context Menu')
        self.setGeometry(300, 300, 300, 220)
        layout = QVBoxLayout()

        self.listWidget = QListWidget()
        for i in range(5):
            self.listWidget.addItem(f'Item {i}')
        self.listWidget.itemClicked.connect(self.on_item_clicked)

        layout.addWidget(self.listWidget)
        self.setLayout(layout)
        self.show()

    def on_item_clicked(self, item):
        # 当用户点击项时，设置当前项为被点击的项
        self.listWidget.setCurrentItem(item)

    def showContextMenu(self, pos):
        # 获取当前选中的项
        current_item = self.listWidget.currentItem()
        if current_item:
            # 创建上下文菜单
            menu = QMenu(self)
            delete_action = menu.addAction("Delete")
            action = menu.exec_(self.listWidget.viewport().mapToGlobal(pos))
            # 如果用户选择了删除操作
            if action == delete_action:
                # 删除当前选中的项
                row = self.listWidget.row(current_item)
                self.listWidget.takeItem(row)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            # 右键点击时显示上下文菜单
            self.showContextMenu(event.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())