from Ui_search_modify import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from database1 import Database

class search_modify(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, header, index, city, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        self.index = index
        self.header = header
        self.city = city
        self.data = []
        self.database = Database()

        self.btnOk.clicked.connect(self.onBtnOk)
        self.btnCancel.clicked.connect(self.onBtnCancel)

        self.lab_example.setText('')
        self.cmb_city.addItem("请选择")
        for item in self.city:
            self.cmb_city.addItem(item)

        # self.search_from_db(self.cmb_city.currentIndex())
        self.cmb_city.currentIndexChanged.connect(lambda: self.search_from_db(self.cmb_city.currentIndex()))

    def search_from_db(self, index):
        self.lab_example.setText('')
        if index != 0:
            region = self.city[index - 1]
            condition_str = '`编码`=' + "%d and " % int(self.index) + '`地域`=' + "'%s'" % region
            # print(self.index)
            # print(region)
            query = 'select * from `Data` where ' + condition_str
            # self.database.get_data(query)
            print("query: ", query)
            try:
                res = self.database.get_data(query)
            except EXECUTE_FAILURE as exef:
                QMessageBox.critical(self, "错误", exef.__str__())
                return
                
            if not res:
                print("no result")
                QMessageBox.warning(self, "警告", '您选择的城市没有相关目录，请转到"添加相关"按钮进行添加。您也可以尝试选择其他城市并在其数据的基础上进行修改。')
                self.cmb_city.setCurrentIndex(0)
            else:
                data = res[0]
                self.data = [data[i] for i in self.header]
                print(self.data)
                self.setUp_table()
        else:
            self.tbw_dialog.clearContents()


    def setUp_table(self):
        self.tbw_dialog.setRowCount(1)
        self.tbw_dialog.setColumnCount(len(self.header))
        self.tbw_dialog.setHorizontalHeaderLabels(self.header)
        self.tbw_dialog.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        if self.data:
            for index in range(len(self.header)):
                data_item = self.data[index]
                # if data_item == None:
                #     data_item = ''
                item = QtWidgets.QTableWidgetItem(str(data_item))
                item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                # if index in [0, 1, 2, 3, 4, 5, 6, 7]:
                #     item.setFlags(QtCore.Qt.ItemIsEditable)
                self.tbw_dialog.setItem(0, index, item)

        else:
            for index in range(len(self.header)):
                if index in [0, 1, 2, 3, 4, 5, 6, 7]:
                    item = QtWidgets.QTableWidgetItem('')
                    item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.tbw_dialog.setItem(0, index, item)
                else:
                    item = QtWidgets.QTableWidgetItem('0.0')
                    item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.tbw_dialog.setItem(0, index, item)

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

    def onBtnOk(self):
        if self.cmb_city.currentIndex() != 0:
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

        else:
            self.lab_example.setText("<font color='red'>  请选择城市进行修改，或点击\"取消\"退出 </font>")
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