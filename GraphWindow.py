# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 776)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("QLabel {  \n"
"        color: rgb(85,85,85); /* 设置标签文本颜色 */ \n"
"        font:12px \\\"Microsoft YaHei\\\"; \n"
"        font-weight:bold; \n"
"    }")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.graphicsView = CustomGraphicsView(Dialog)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setStyleSheet("background-color: rgba(89, 217, 212, 50);\n"
"border-radius: 20px;")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(47, 125, 238, 90);\n"
"        border-radius:3px; \n"
"        min-height:30px; \n"
"        min-width:60px; \n"
"        font:13px \\\"Microsoft YaHei\\\";\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color:rgba(85, 255, 255, 50);\n"
"    }\n"
"QPushButton:pressed {\n"
"  background-color:rgba(90,216,212,50);\n"
"  color:rgb(40,92,90);\n"
"    }")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgba(47, 125, 238, 90);\n"
"        border-radius:3px; \n"
"        min-height:30px; \n"
"        min-width:60px; \n"
"        font:13px \\\"Microsoft YaHei\\\";\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color:rgba(85, 255, 255, 50);\n"
"    }\n"
"QPushButton:pressed {\n"
"  background-color:rgba(90,216,212,50);\n"
"  color:rgb(40,92,90);\n"
"    }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept) # type: ignore
        self.pushButton_2.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择参照图片"))
        self.label.setText(_translate("Dialog", "请拖拽参照图片到此处："))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
from CustomGraphicsView import CustomGraphicsView