# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoiWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 180)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setStyleSheet("QComboBox{\n"
"\n"
"    font-size:14px \\\"Microsoft YaHei\\\";\n"
"    padding: 1px 15px 1px 3px;\n"
"    border:2px solid rgba(89, 217, 212, 50); /* 设置输入框边框 */\n"
"    border-radius:5px 5px 0px 0px;\n"
"} \n"
"/*下拉按钮*/\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border:none;\n"
"}\n"
"/*箭头图标*/\n"
"QComboBox::down-arrow {\n"
"    /*image: url(:/res/work/dateDown.png);*/\n"
"}\n"
"/*下拉列表*/\n"
"QComboBox QAbstractItemView{\n"
"    background:rgba(255, 255, 255, 50);\n"
"    border:1px solid rgba(255, 255, 255, 50);\n"
"    border-radius:5px 5px 5px 5px;\n"
"    font-size:14px;\n"
"    outline: 0px;  \n"
"}\n"
"QComboBox QAbstractItemView::item{\n"
"    height:36px;\n"
"    color:rgba(255, 255, 255, 50);\n"
"    padding-left:9px;\n"
"    background-color:rgba(255, 255, 255, 50);\n"
"}\n"
"QComboBox QAbstractItemView::item:hover{ \n"
"    background-color:rgba(89, 217, 212, 50);\n"
"\n"
"}\n"
"QComboBox QAbstractItemView::item:selected{\n"
"    background-color:rgba(89, 217, 212, 50);\n"
"\n"
"}\n"
"QComboBox:on { \n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/waves-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/waves-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        self.verticalLayout.addWidget(self.comboBox)
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
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
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
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
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
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.comboBox.currentIndexChanged['int'].connect(Dialog.on_combobox_current_index_changed) # type: ignore
        self.pushButton.clicked.connect(Dialog.accept) # type: ignore
        self.pushButton_1.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择噪声类型"))
        self.label.setText(_translate("Dialog", "请选择加噪类型："))
        self.comboBox.setItemText(0, _translate("Dialog", "椒盐噪声"))
        self.comboBox.setItemText(1, _translate("Dialog", "高斯噪声"))
        self.lineEdit_1.setPlaceholderText(_translate("Dialog", "请输入噪声的比例，默认0.05"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "请输入噪声的均值，默认0"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "请输入噪声的方差，默认0.05"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_1.setText(_translate("Dialog", "取消"))
