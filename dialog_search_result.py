from Ui_dialog_search_result import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
# from database import Database
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QCheckBox, QGridLayout, QTreeWidgetItem, QLabel, QLineEdit, QDialog, QMessageBox

class dialog_search_result(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.btnOk.clicked.connect(self.on_btnOk)
        self.bnt_close.clicked.connect(self.on_btnOk)
        self.data = []
        self.tbw_result.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)

    def on_btnOk(self):
        self.close()

    def setupTbw(self, data):
        # self.tbw_result.clear()
        # print(1)
        self.data = data
        self.tbw_result.setRowCount(len(data))
        self.tbw_result.setColumnCount(2)
        self.tbw_result.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header = ['相关路径','操作']
        self.tbw_result.setHorizontalHeaderLabels(header)
        for path_index in range(len(data)):
            path_name = ''
            for i in range(len(data[path_index])):
                point = data[path_index][i]
                path_name += point
                if i != len(data[path_index]) - 1:
                    path_name += ' > '

            item = QtWidgets.QTableWidgetItem(path_name)
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tbw_result.setItem(path_index, 0, item)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def modify_data(self, id, modify_data, mode):
        self.data[id] = []
        for i in range(2, 7):
            self.data[id].append(modify_data[i])
        self.data[id].append(modify_data[0] + ' ' + modify_data[7])
        
        path_name = ''
        for x in range(len(self.data[id])):
            path_name += self.data[id][x]
            if x != len(self.data[id]) - 1:
                path_name += ' > '
        if mode == 0:
            path_name += '(%s已修改)' % modify_data[1]
        else:
            path_name += '(%s已添加)' % modify_data[1]
            
        item = QtWidgets.QTableWidgetItem(path_name)
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.tbw_result.setItem(id, 0, item)