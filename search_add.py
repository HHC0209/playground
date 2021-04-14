from Ui_search_add import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# from database import Database

class search_add(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, header, data, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        self.header = header
        self.data = data

        self.setUp_table()
        self.lab_example.setText('')
        self.btnCityOk.clicked.connect(self.onBtnCityOk)
        self.btnOk.clicked.connect(self.onBtnOk)
        self.btnCancel.clicked.connect(self.onBtnCancel)

    def setUp_table(self):
        self.tbw_dialog.setRowCount(1)
        self.tbw_dialog.setColumnCount(len(self.header))
        self.tbw_dialog.setHorizontalHeaderLabels(self.header)
        self.tbw_dialog.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        for i in range(len(self.data)):
            data_item = self.data[i]
            item = QtWidgets.QTableWidgetItem(data_item)
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tbw_dialog.setItem(0, i + 2, item)

        for i in range(2):
            item = QtWidgets.QTableWidgetItem('')
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tbw_dialog.setItem(0, i, item)

        for i in range(8, len(self.header)):
            item = QtWidgets.QTableWidgetItem('0.0')
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tbw_dialog.setItem(0, i, item)

    def onBtnCityOk(self):
        text = self.le_city.text()
        if text == '':
            self.lab_example.setText("<font color='red'>   请输入城市。</font>")
        else:
            item = QtWidgets.QTableWidgetItem(text)
            self.tbw_dialog.setItem(0, 1, item)

    def onBtnOk(self):
        empty = []
        for index in range(0, 8):
            if not self.tbw_dialog.item(0, index).text():
                empty.append(self.header[index])

        if empty:
            temp = ''
            for item in empty:
                temp += (item + ' ')
            self.lab_example.setText("<font color='red'>   %s不能为空！</font>" % temp)
        else:
            self.accept()

        # self.lab_example.setText("<font color='red'>  请选择城市进行修改，或点击\"取消\"退出 </font>")
        # QMessageBox.warning(self, "警告", '请选择城市进行修改，或点击"取消"退出')

    def onBtnCancel(self):
        self.reject()

    def get_data(self):
        data = []
        for i in range(len(self.header)):
            item = self.tbw_dialog.item(0, i)
            # if item == None:
            #     data.append("数据暂无")
            # else:
            data.append(item.text())
        return data