from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from tbw_item import tbw_item
from detail_dialog import detail_dialog
# from influxdb import InfluxDBClient
# from database import Database
from ui_dialog_1 import Dialog_1
# from mainwindow import Ui_MainWindow
import xlwt


class TableWidgetSearch:
    def __init__(self, widget):
        self.datas = []    #包含了表格的各行，类型为tbw_item。
        self.selected_year = []
        self.widget = widget
        self.contain = []
        # self.database = Database()  # 初始化数据库
        self.modify_for_row = []
        self.detail_for_row = []

    def view_detail(self, id):
        dialog_detail = detail_dialog(id = id, item = self.datas[id])
        name = self.datas[id].realname
        dialog_detail.setTitle(name)
        dialog_detail.setInfo("Here are some information.")
        dialog_detail.exec_()

    # def reload_after_modify(self, data, modified_data, year):
    #     index = modified_data[0]
    #     region = modified_data[1]

    #     is_exist, old_ctg1, old_ctg2, old_ctg3, old_ctg4, old_ctg5, old_final_name = ui_mainwindow.is_category_exist(
    #         index, region)

    #     ui_mainwindow.delete_category(region, data[2], data[3], data[4], data[5], data[6], '%s %s' % (data[0], data[7]))
    #     # self.delete_data(data[0], data[1])
    #     self.database.delete_data(data[0], data[1])
    #     if is_exist:
    #         ui_mainwindow.delete_category(region, old_ctg1, old_ctg2, old_ctg3, old_ctg4, old_ctg5, old_final_name)
    #         # self.delete_data(index, region)
    #     ui_mainwindow.form_category_structure([modified_data])
    #     # self.tbw_search_class.widget.clearSelection()
    #     # self.tbw_search_class.add_data_dialog(modified_data)
    #     # self.tbw_search_class.display()
    #     self.database.add_data_dialog(modified_data, year)

    #     if modified_data[1] not in ui_mainwindow.region:
    #         ui_mainwindow.region.append(modified_data[1])
    #         ui_mainwindow.clear_gridLayout(ui_mainwindow.glo_city_search)  # 清空gridLayout
    #         ui_mainwindow.clear_gridLayout(ui_mainwindow.glo_city_process)  # 清空gridLayout
    #         ui_mainwindow.initialize_gridLayout(ui_mainwindow.glo_city_search, ui_mainwindow.region)  # 按照新的self.region更新gridLayout
    #         ui_mainwindow.initialize_gridLayout(ui_mainwindow.glo_city_process, ui_mainwindow.region)  # 按照新的self.region更新gridLayout
    #     ui_mainwindow.update_file()  # 更新year.cfg region.cfg

    #     ui_mainwindow.trw_search.clear()
    #     ui_mainwindow.trw_process.clear()
    #     ui_mainwindow.initiate_treeWidget(self.trw_search)
    #     ui_mainwindow.initiate_treeWidget(self.trw_process)

    # def modify(self, id):
    #     item = self.datas[id]

    #     # rowcnt = len(item.index)
    #     header = ['编码', '地域', '级别1', '级别2', '级别3', '级别4', '级别5', '级别6']
    #     for year in item.year:
    #         header.append(year)
        
    #     data = []
    #     region = item.data[0]['地域']
        
    #     for i in item.index:
    #         condition_str = '"编码"=' + "'%s' and " % i + '"地域"=' + "'%s'" % region
    #         query = 'select * from Data where ' + condition_str
    #         result = self.database.get_data(query)[0]
    #         data.append([result[i] for i in header])

    #     dialog_1 = Dialog_1(1, header, data=data)
    #     if dialog_1.exec_() == 1:
    #         modified_data = dialog_1.get_data()  #修改后的表格中的数据
    #         item_data = item.data
    #         for i in range(len(item_data)):
    #             for j in range(len(header)):
    #                 item_data[i][header[j]] = modified_data[i][j]
            
    #         item.setRealName()
    #         self.refresh(id)
            
    #         from ui_mainwindow import MainWindow
    #         wind = MainWindow()
    #         for i in range(len(data)):           #修改前的表格中的数据
    #             wind.reload_after_modify(data[i], modified_data[i], item.year)

    def buttonForRow(self, id):
        widget = QWidget()

        detailBtn = QPushButton("查看详情")
        detailBtn.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(75, 225, 75); font-family:'微软雅黑'; font-Point Size:10")
        detailBtn.clicked.connect(lambda:self.view_detail(id))
        self.detail_for_row.append(detailBtn)

        modifyBtn = QPushButton("修正")
        modifyBtn.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(225, 174, 0); font-family:'微软雅黑'; font-Point Size:10")
        self.modify_for_row.append(modifyBtn)
        modifyBtn.clicked.connect(lambda:self.modify(id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(detailBtn)
        hLayout.addWidget(modifyBtn)
        hLayout.setContentsMargins(5,2,5,2)
        widget.setLayout(hLayout)

        return widget

    def clear(self):
        self.widget.clear()
        self.datas = []
        self.selected_year = []
        self.widget.setRowCount(0)
        self.widget.setColumnCount(0)

    def add_data(self, datas, selected_years):
        self.datas = datas
        self.selected_year = selected_years
        for i in range(len(self.datas)):
            datas[i].setRow(i)
            datas[i].setRealName()

    def add_data_dialog(self, data):
        flag = -1
        for index, d in enumerate(self.datas):
            if d['编码'] == data[0] and d['地域'] == data[1]:
                flag = index

        if flag >= 0:
            # 6个级别 从第2列开始
            for cat_index in range(2, 8):
                self.datas[flag]['级别%d' % (cat_index - 1)] = data[cat_index]
            # 从第8列开始
            for year_index in range(len(self.selected_year)):
                value = data[8+year_index]
                self.datas[flag][self.selected_year[year_index]] = value
        else:
            temp = {}
            for i in range(len(self.header)):
                temp[self.header[i]] = data[i]
            self.datas.append(temp)

    def delete_data(self, index, region):
        for i in range(len(self.datas)):
            if self.datas[i]['编码'] == index and self.datas[i]['地域'] == region:
                del self.datas[i]
                break


    def display(self):
        self.widget.clear()
        self.widget.setRowCount(len(self.datas))
        self.widget.setColumnCount(2)
        self.header = ['路径','操作']
        self.widget.setHorizontalHeaderLabels(self.header)
        self.widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        row = 0
        col = 0
        for point in self.datas:
            item = QtWidgets.QTableWidgetItem(point.realname)
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.widget.setItem(row, col, item)
            row += 1

        # col = 1
        # for i in range(self.widget.rowCount()):
        #     self.widget.setCellWidget(i, col, self.buttonForRow(i))

        # for i in range(self.widget.rowCount()):
        #     print(self.detail_for_row[i])
        #     print(self.modify_for_row[i])
            # self.widget_for_row.append(self.buttonForRow(i))
        # row = 0
        # for point in self.datas:
        #     col = 0
        #     for key in self.header[:8]:
        #         item = QtWidgets.QTableWidgetItem(point[key])
        #         item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        #         self.widget.setItem(row, col, item)
        #         col += 1
        #     for key in self.header[8:]:
        #         # try to fix it (whh)
        #         if point[key] == None:
        #             item = QtWidgets.QTableWidgetItem("")
        #         else:
        #             item = QtWidgets.QTableWidgetItem(str(round(float(point[key]), 2)))
        #         item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        #         self.widget.setItem(row, col, item)
        #         col += 1
        #     row += 1

    def export_excel(self, filepath):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Data')

        style_hv = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = '微软雅黑'

        alignment_hv = xlwt.Alignment()
        alignment_hv.horz = xlwt.Alignment.HORZ_CENTER
        alignment_hv.vert = xlwt.Alignment.VERT_CENTER

        style_hv.alignment = alignment_hv
        style_hv.font = font

        worksheet.write(0, 0, '编码', style_hv)
        worksheet.write(0, 1, '地域', style_hv)
        for i in range(1, 7):
            worksheet.write(0, 1+i, '级别%d' % i, style_hv)
        for year_index in range(len(self.selected_year)):
            worksheet.write(0, 8+year_index, self.selected_year[year_index], style_hv)

        # sum = 0
        # for item in self.datas:
        #     sum += len(item.data)
        # print(sum)

        row = 1
        for item in self.datas:
            for record in item.data:
                col = 0
                for key in record.keys():
                    if key == 'time':
                        continue
                    if key in ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']:
                        print(key)
                        if key in self.selected_year:
                            data = record[key]
                        else:
                            continue
                    else:
                        data = record[key]
                    try:
                        data = float(data)
                    except ValueError:
                        pass
                    worksheet.write(row, col, data, style_hv)
                    col += 1
                row += 1
        # for row in range(sum):
        # # for row in range(len(self.datas)):
        #     for col in range(len(self.datas[0].data[0].keys())-1):
        #         data = self.widget.item(row, col).text()
        #         try:
        #             data = float(data)
        #         except ValueError:
        #             pass
        #         worksheet.write(row+1, col, data, style_hv)

        worksheet.col(0).width = 3000
        worksheet.col(1).width = 3000
        for col in range(2, 8):
            worksheet.col(col).width = 6200
        for col in range(8, 8 + len(self.selected_year) + 1):
        # for col in range(8, len(self.datas[0].keys())-1):
            worksheet.col(col).width = 3000
        workbook.save(filepath)

    def refresh(self, id):
        item = QtWidgets.QTableWidgetItem(self.datas[id].realname)
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.widget.setItem(id, 0, item)
