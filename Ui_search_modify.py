# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\pyqt5\project_developing\search_modify.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 180)
        Dialog.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.tbw_dialog = QtWidgets.QTableWidget(Dialog)
        self.tbw_dialog.setGeometry(QtCore.QRect(10, 60, 880, 75))
        self.tbw_dialog.setObjectName("tbw_dialog")
        self.tbw_dialog.setColumnCount(0)
        self.tbw_dialog.setRowCount(0)
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(720, 145, 80, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(810, 145, 80, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 371, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cmb_city = QtWidgets.QComboBox(Dialog)
        self.cmb_city.setGeometry(QtCore.QRect(410, 20, 100, 25))
        self.cmb_city.setObjectName("cmb_city")
        self.lab_example = QtWidgets.QLabel(Dialog)
        self.lab_example.setGeometry(QtCore.QRect(10, 146, 400, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lab_example.setFont(font)
        self.lab_example.setObjectName("lab_example")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnOk.setText(_translate("Dialog", "确定"))
        self.btnCancel.setText(_translate("Dialog", "取消"))
        self.label.setText(_translate("Dialog", "修改相关——请选择您要修改的路径所属的城市"))
        self.lab_example.setText(_translate("Dialog", "TextLabel"))
