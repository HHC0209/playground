import sys
from PyQt5 import QtWidgets
from ui_mainwindow import MainWindow
import sympy
import plotly
import os
import pymysql

if __name__ == '__main__':
    # print(type(os.getcwd()))
    app = QtWidgets.QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    myWin.check_network()
    # try:
    #     pymysql.connect(host="gz-cynosdbmysql-grp-0965sb99.sql.tencentcdb.com", user="root", password="A1b1c1d1", db="test", port=25462,charset='utf8')
    # except:
    #     myWin.network_exception()
    sys.exit(app.exec_())

# pyuic5 -o mainwindow.py mainwindow.ui
# pyinstaller -F main.py --noconsole
# pyinstaller -D main.py --noconsole

# 加载spec里面
# import sys
# sys.setrecursionlimit(5000)