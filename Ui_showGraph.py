# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\pyqt5\project_developing\showGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.sca_plot = QtWidgets.QScrollArea(Dialog)
        self.sca_plot.setGeometry(QtCore.QRect(0, 30, 1200, 760))
        self.sca_plot.setWidgetResizable(True)
        self.sca_plot.setObjectName("sca_plot")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1198, 758))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sca_plot.setWidget(self.scrollAreaWidgetContents)
        self.bnt_close = QtWidgets.QPushButton(Dialog)
        self.bnt_close.setGeometry(QtCore.QRect(1170, 0, 30, 30))
        self.bnt_close.setMinimumSize(QtCore.QSize(30, 30))
        self.bnt_close.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.bnt_close.setFont(font)
        self.bnt_close.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(217, 0, 0);")
        self.bnt_close.setObjectName("bnt_close")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.bnt_close.setText(_translate("Dialog", "×"))