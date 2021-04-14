from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
# from database1 import Database
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QCheckBox, QGridLayout, QTreeWidgetItem, QLabel, QLineEdit, QDialog, QMessageBox
from Ui_detail_dialog import Ui_Dialog
from ui_dialog_1 import Dialog_1
from ERRORS import NETWORK_ERR, INSERT_FAILURE, UPDATE_FAILURE, EXECUTE_FAILURE


class detail_dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, id, item, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.id = id
        # QtWidgets.QApplication.setStyle('Fusion')  # ui风格为Fusion
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 无标题栏
        self.item = item
        # self.database = Database()
        self.title = ''
        self.info = ''
        self.detail_path = []
        self.btnOk.clicked.connect(self.ok_clicked)
        # self.btnModi.clicked.connect(self.modify_clicked)
        self.btn_close.clicked.connect(self.close_clicked)
        self.tbw_info.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)

    def setTitle(self, title):
        self.title = title + "查询详情"
        self.titleLb.setText(self.title)
        self.titleLb.setWordWrap(True)
        # self.titleLb.setAlignment(QtCore.AlignTop)
        # self.titleLb.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    # def setInfo(self, info):
    #     self.info = info
        # self.infoLb.setText(self.info)

    def set_detail_path(self):
        name = self.item.name[-1]
    
        for item in self.item.data:
            cnt = 0
            for i in range(1, 7):
                query = "级别%d" % i
                if item[query] == name:
                    cnt = i
                    break
            if cnt == 6:
                self.detail_path.append(self.item.realname)
            else:
                cnt1 = cnt + 1
                query = "级别%d" % cnt1
                tmp = item[query]
                if cnt1 + 1 <= 6:
                    for i in range(cnt1 + 1, 7):
                        query = "级别%d" % i
                        j = i - 1
                        post_query = "级别%d" % j
                        if item[query] != item[post_query]:
                            tmp += ", " + item[query]
                self.detail_path.append(tmp)

    def table_display(self):   #展示详情的tablewidget
        self.tbw_info.clear()
        self.tbw_info.setRowCount(len(self.item.data))
        self.header = ['明细']
        for i in self.item.year:
            self.header.append(i)

        self.tbw_info.setColumnCount(len(self.header))
        self.tbw_info.setHorizontalHeaderLabels(self.header)
        self.tbw_info.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.set_detail_path()
        for i in range(0, len(self.detail_path)):
            # print(self.detail_path[i])
            item = QtWidgets.QTableWidgetItem(self.detail_path[i])
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tbw_info.setItem(i, 0, item)

        for i in range(1, len(self.header)):
            year = self.tbw_info.horizontalHeaderItem(i).text()
            for j in range(0, len(self.item.data)):
                res = self.item.data[j][year]
                item = QtWidgets.QTableWidgetItem(res)
                item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tbw_info.setItem(j, i, item)



    def ok_clicked(self):
        self.close()
    
    def close_clicked(self):
        self.close()

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

    # def modify_clicked(self):
    #     item = self.item
    #     header = ['编码', '地域', '级别1', '级别2', '级别3', '级别4', '级别5', '级别6']
    #     for year in item.year:
    #         header.append(year)
        
    #     data = []
    #     region = item.data[0]['地域']
        
    #     for i in item.index:
    #         condition_str = '"编码"=' + "'%s' and " % i + '"地域"=' + "'%s'" % region
    #         query = 'select * from Data where ' + condition_str
    #         try:
    #             result = self.database.get_data(query)[0]
    #         except EXECUTE_FAILURE as exef:
    #             QMessageBox.critical(self, '错误', exef.__str__())
    #             return
                
    #         data.append([result[i] for i in header])

    #     dialog_1 = Dialog_1(1, header, data=data)
    #     self.close()
    #     dialog_1.exec_()