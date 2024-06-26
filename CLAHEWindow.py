# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CLAHEWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("QLabel {  \n"
"        color: rgb(85,85,85); /* 设置标签文本颜色 */ \n"
"        font:12px \\\"Microsoft YaHei\\\"; \n"
"        font-weight:bold; \n"
"    }")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_1.setStyleSheet("QLineEdit {  \n"
"    border:2px solid rgba(89, 217, 212, 50); /* 设置输入框边框 */\n"
"    padding-left:10px;\n"
"    border-radius:3px; /* 设置输入框边框圆角 */  \n"
"    color:rgb(105,105,105);\n"
"    font:13px;\n"
"    font-size: 12pt \\\"Microsoft YaHei\\\"; /* 设置字体大小 */  \n"
"    padding: 4px; /* 设置内边距 */  \n"
"}  \n"
"QLineEdit:hover { /* 鼠标悬浮在QLineEdit时的状态 */\n"
"    border: 1px solid #298DFF;\n"
"    border-radius: 3px;\n"
"    background-color: #F2F2F2;\n"
"    color: #298DFF;\n"
"    selection-background-color: #298DFF;\n"
"    selection-color: #F2F2F2;\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgba(89, 217, 212, 50);\n"
"}\n"
"QLineEdit:disabled{\n"
"    background-color:rgb(238,238,238);\n"
"}")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout_2.addWidget(self.lineEdit_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("QLabel {  \n"
"        color: rgb(85,85,85); /* 设置标签文本颜色 */ \n"
"        font:12px \\\"Microsoft YaHei\\\"; \n"
"        font-weight:bold; \n"
"    }")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setStyleSheet("QLineEdit {  \n"
"    border:2px solid rgba(89, 217, 212, 50); /* 设置输入框边框 */\n"
"    padding-left:10px;\n"
"    border-radius:3px; /* 设置输入框边框圆角 */  \n"
"    color:rgb(105,105,105);\n"
"    font:13px;\n"
"    font-size: 12pt \\\"Microsoft YaHei\\\"; /* 设置字体大小 */  \n"
"    padding: 4px; /* 设置内边距 */  \n"
"}  \n"
"QLineEdit:hover { /* 鼠标悬浮在QLineEdit时的状态 */\n"
"    border: 1px solid #298DFF;\n"
"    border-radius: 3px;\n"
"    background-color: #F2F2F2;\n"
"    color: #298DFF;\n"
"    selection-background-color: #298DFF;\n"
"    selection-color: #F2F2F2;\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgba(89, 217, 212, 50);\n"
"}\n"
"QLineEdit:disabled{\n"
"    background-color:rgb(238,238,238);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("QLabel {  \n"
"        color: rgb(85,85,85); /* 设置标签文本颜色 */ \n"
"        font:12px \\\"Microsoft YaHei\\\"; \n"
"        font-weight:bold; \n"
"    }")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setStyleSheet("QLineEdit {  \n"
"    border:2px solid rgba(89, 217, 212, 50); /* 设置输入框边框 */\n"
"    padding-left:10px;\n"
"    border-radius:3px; /* 设置输入框边框圆角 */  \n"
"    color:rgb(105,105,105);\n"
"    font:13px;\n"
"    font-size: 12pt \\\"Microsoft YaHei\\\"; /* 设置字体大小 */  \n"
"    padding: 4px; /* 设置内边距 */  \n"
"}  \n"
"QLineEdit:hover { /* 鼠标悬浮在QLineEdit时的状态 */\n"
"    border: 1px solid #298DFF;\n"
"    border-radius: 3px;\n"
"    background-color: #F2F2F2;\n"
"    color: #298DFF;\n"
"    selection-background-color: #298DFF;\n"
"    selection-color: #F2F2F2;\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgba(89, 217, 212, 50);\n"
"}\n"
"QLineEdit:disabled{\n"
"    background-color:rgb(238,238,238);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept) # type: ignore
        self.pushButton_2.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "输入自适应参数"))
        self.label.setText(_translate("Dialog", "对比度限制："))
        self.lineEdit_1.setPlaceholderText(_translate("Dialog", "默认40.0"))
        self.label_3.setText(_translate("Dialog", "网格大小："))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "默认8"))
        self.label_4.setText(_translate("Dialog", "×"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "默认8"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
