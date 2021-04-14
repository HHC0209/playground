import pymysql
import datetime
import json
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
from ERRORS import NETWORK_ERR, INSERT_FAILURE, UPDATE_FAILURE, EXECUTE_FAILURE

class Database:
    # def __init__(self):

        # try:
        #     self.connect_to_database()
        # except:
        #     raise NETWORK_ERR()
        # try:
        # self.db = pymysql.connect(host="gz-cynosdbmysql-grp-0965sb99.sql.tencentcdb.com", user="root", password="A1b1c1d1", db="test", port=25462,charset='utf8')
        # self.cr = self.db.cursor(cursor = pymysql.cursors.DictCursor)
        # except:
        #     # QMessageBox.warning(self, "警告", "网络连接失败，请重试")
        #     font = QtGui.QFont()
        #     font.setFamily("微软雅黑")
        #     font.setPointSize(10)
        #     messagebox = QMessageBox(QMessageBox.Warning, '警告','无法连接网络，请重试')
        #     messagebox.setFont(font)
        #     Qyes = messagebox.addButton(self.tr("重试"), QMessageBox.YesRole)
        #     Qno = messagebox.addButton(self.tr("取消"), QMessageBox.NoRole)
        #     messagebox.exec_()
        #     if messagebox.clickedButton() == Qyes:
        #         if self.retry_connect():
        #             messagebox.exec_()
        #     else:
        #         messagebox.close()
    def check_network(self):
        try:
            self.db = pymysql.connect(host="gz-cynosdbmysql-grp-0965sb99.sql.tencentcdb.com", user="root", password="A1b1c1d1", db="test", port=25462,charset='utf8')
            self.cr = self.db.cursor(cursor = pymysql.cursors.DictCursor)
        except:
            raise NETWORK_ERR()


    def connect_to_database(self):
        self.db = pymysql.connect(host="gz-cynosdbmysql-grp-0965sb99.sql.tencentcdb.com", user="root", password="A1b1c1d1", db="test", port=25462,charset='utf8')
        self.cr = self.db.cursor(cursor = pymysql.cursors.DictCursor)
    
    def add_data_excel(self, worksheet, year_list):
        # query = 'select * from "Data"'
        # points = self.get_data(query)
        # temp = {}
        # for point in points:
        #     temp['%s %s' % (point['编码'], point['地域'])] = point['time']

        # temp_time = datetime.datetime.now()
        json_body = []
        # 数据从excel的第2行开始
        for row_num in range(1, worksheet.nrows):
            row = worksheet.row_values(row_num)  # 读取excel的一行
            # dict_tag = {}
            # dict_tag['编码'] = str(int(row[0]))
            # dict_tag['地域'] = row[1]

            dict_field = {}
            dict_field['编码'] = str(int(row[0]))
            dict_field['地域'] = row[1]
            # 6个级别 从第2列开始
            # 尝试字符串化 (whh)
            for cat_index in range(2, 8):
                dict_field['级别%d' % (cat_index-1)] = str(row[cat_index])
                # dict_field['级别%d' % (cat_index-1)] = row[cat_index]
            # max_year-min_year个年份 从第8列开始
            tmp_year = {}
            for year_index in range(len(year_list)):
                try:
                    value = str(float(row[8 + year_index]))
                except:
                    value = '0'
                
                tmp_year[year_list[year_index]] = value
            
            jsn_year = json.dumps(tmp_year)
            dict_field['年份'] = jsn_year
                # dict_field[year_list[year_index]] = value


            # dict_record = {}
            # dict_record['tags'] = dict_tag
            # dict_record['fields'] = dict_field
            # dict_record['measurement'] = 'Data'

            # try:
            #     dict_record['time'] = temp['%s %s' % (dict_tag['编码'], dict_tag['地域'])]
            # except:
            #     temp_time += datetime.timedelta(microseconds=5)
            #     dict_record['time'] = temp_time.isoformat()

            json_body.append(dict_field)
        # self.client.write_points(json_body)
        # try:
        #     self.connect_to_database()
        # except:
        #     raise NETWORK_ERR()
        sql = "INSERT INTO `Data` (`地域`, `编码`, `级别1`, `级别2`, `级别3`, `级别4`, `级别5`, `级别6`, `年份`) VALUES "
            
        for i in range(len(json_body)):
            dict_field = json_body[i]
            # print(dict_field)
            if i != 0:
                sub_str = ',('
            else:
                sub_str = '('
            # sql = "INSERT INTO `Data` (`地域`, `编码`, `级别1`, `级别2`, `级别3`, `级别4`, `级别5`, `级别6`, `年份`) VALUES ("
            sub_str += "'%s'," % dict_field["地域"]
            sub_str += "%d," % int(dict_field["编码"])
            for i in range(1, 7):
                ind = "级别%d" % i
                item = dict_field[ind]
                if isinstance(item, str):
                    sub_str += "'%s'" % item
                    sub_str += ","
                else:
                    sub_str += dict_field[ind]

            sub_str += "'%s'" % dict_field["年份"]
            sub_str += ")"

            sql += sub_str

        # print("=======================================")
        # print('sql:', sql)
        try:
            self.connect_to_database()
            self.cr.execute(sql)
            self.db.commit()
        except:
            raise INSERT_FAILURE()
        # except:
        #     raise NETWORK_ERR()
    
            # sql = 'INSERT INTO "Data" ("地域", "编码", "级别1", "级别2", "级别3", "级别4", "级别5", "级别6", "年份") VALUES (dict_field["地域"], dict_field["编码"], dict_field["级别1"], dict_field["级别2"], dict_field["级别3"], dict_field["级别4"], dict_field["级别5"], dict_field["级别6"], dict_field["年份"])'
            # sql = "INSERT INTO `Data` (`地域`, `编码`, `级别1`, `级别2`, `级别3`, `级别4`, `级别5`, `级别6`, `年份`) VALUES ('广州', 222222, 'a', 'b', 'c', 'd', 'e', 'f', '{\"2011\":\"111\", \"2012\":\"222\"}')"
            # self.cr.execute(sql)

        # sql = "INSERT INTO `Data` (`地域`, `编码`, `级别1`, `级别2`, `级别3`, `级别4`, `级别5`, `级别6`, `年份`) VALUES ('深圳', 33333, 'a', 'b', 'c', 'd', 'e', 'f', '{\"2011\":\"111\", \"2012\":\"222\"}')"

    def add_data_dialog(self, data, years):
        # self.retry_connect()
        # query = 'select * from "Data"'
        # points = self.get_data(query)
        # temp = {}
        # for point in points:
        #     temp['%s %s' % (point['编码'], point['地域'])] = point['time']

        # temp_time = datetime.datetime.now()
        # dict_tag = {}
        # dict_tag['编码'] = data[0]
        # dict_tag['地域'] = data[1]

        dict_field = {}
        dict_field['编码'] = data[0]
        dict_field['地域'] = data[1]
        # 6个级别 从第2列开始
        for cat_index in range(2, 8):
            dict_field['级别%d' % (cat_index - 1)] = data[cat_index]
        # 从第8列开始
        tmp_year = {}
        for year_index in range(len(years)):
            value = data[8+year_index]
            tmp_year[years[year_index]] = value
            # dict_field[years[year_index]] = value

        jsn_year = json.dumps(tmp_year)
        dict_field['年份'] = jsn_year
        
        sql = "INSERT INTO `Data` (`地域`, `编码`, `级别1`, `级别2`, `级别3`, `级别4`, `级别5`, `级别6`, `年份`) VALUES ("
        sql += "'%s'," % dict_field["地域"]
        sql += "%d," % int(dict_field["编码"])
        for i in range(1, 7):
            ind = "级别%d" % i
            item = dict_field[ind]
            if isinstance(item, str):
                sql += "'%s'" % item
                sql += ","
            else:
                sql += dict_field[ind]
                sql += ","

        sql += "'%s'" % dict_field["年份"]
        sql += ")"
        # print("=====================================")
        # print("sql: ", sql)
        # sql1 = 'INSERT INTO Data (地域, 编码, 级别1, 级别2, 级别3, 级别4, 级别5, 级别6, 年份) VALUES (dict_field["地域"], dict_field["编码“], dict_field["级别1"], dict_field["级别2"], dict_field["级别3"], dict_field["级别4"], dict_field["级别5"], dict_field["级别6"], dict_field["年份"])'
        
        # print("sql: ", sql)
        # print("sql1: ", sql1)
        try:
            self.connect_to_database()
            self.cr.execute(sql)
            self.db.commit()
        except:
            raise INSERT_FAILURE
        # dict_record = {}
        # dict_record['tags'] = dict_tag
        # dict_record['fields'] = dict_field
        # dict_record['measurement'] = 'Data'

        # try:
        #     dict_record['time'] = temp['%s %s' % (dict_tag['编码'], dict_tag['地域'])]
        # except:
        #     dict_record['time'] = temp_time.isoformat()


        # self.client.write_points([dict_record])


    def modify_data(self, place, modified_data, header):
        query_list = []
        for item in place:
            region = modified_data[item[0]][1]
            index = modified_data[item[0]][0]
            if item[1] <= 7:
                modify_item = header[item[1]]
                sql = "UPDATE `Data` SET `%s`='%s' WHERE `地域`='%s' AND `编码`='%d'" % (modify_item, modified_data[item[0]][item[1]], region, int(index))

            else:
                query = "SELECT `年份` from `Data` WHERE `地域`='%s' AND `编码`='%d'" % (region, int(index))
                # print(query)
                self.cr.execute(query)
                result = self.cr.fetchall()[0]['年份']
                # print(result)
                # print(type(result))
                dic = json.loads(result)
                for i in range(8, len(header)):
                    dic[header[i]] = modified_data[item[0]][i]
                json_year = json.dumps(dic)
                sql = "UPDATE `Data` SET `年份`='%s' WHERE `地域`='%s' AND `编码`='%d'" % (json_year, region, int(index))
                # print("sql: ", sql)

            query_list.append(sql)
        
        for query in query_list:
            try:
                self.connect_to_database()
                self.cr.execute(sql)
                self.db.commit()
            except:
                raise UPDATE_FAILURE()


    def delete_data(self, index, region):
        query = "DELECT FROM `Data` WHERE `编码`='%d' AND `地域`='%s'" % (int(index), region)
        # query = 'delete from Data where "编码"=' + "'%s'" % index + 'and "地域"=' + "'%s'" % region
        try:
            self.cr.execute(query)
            self.db.commit()
        except:
            raise EXECUTE_FAILURE()

    def get_data(self, query):
        try:
            self.connect_to_database()
            self.cr.execute(query)
        except:
            raise EXECUTE_FAILURE()
            return

        result = self.cr.fetchall()
        print(result)

        for item in result:
            year = eval(item.pop("年份"))
            item = item.update(year)

        # print("resut in database1 > get_data")
        # print(result)
        # print("\n\n")
        return result
        # points = list(result.get_points())
        # return points
    def empty_table(self):
        sql = "truncate table `Data`"
        try:
            self.connect_to_database()
            self.cr.execute(sql)
            self.db.commit()
        except:
            raise EXECUTE_FAILURE()
# SQL = 'INSERT INTO test1(col1) VALUES(12)'
# cr.execute(SQL)
# db.commit()
# result = cr.fetchall()
# print(result)
# db.close()

# if __name__ == '__main__':
#     db = Database()
#     sql = 'INSERT INTO Data (地域, 编码) VALUES ("汕头", 11111)'
#     # db.cr.execute(sql)
#     s = 'SELECT * from Data'
#     db.cr.execute(s)
#     result = db.cr.fetchall()

#     for item in result:
#         year = eval(item.pop("年份"))
#         item = item.update(year)

#     print(result)

    def retry_connect(self):
        try:
            self.db = pymysql.connect(host="gz-cynosdbmysql-grp-0965sb99.sql.tencentcdb.com", user="root", password="A1b1c1d1", db="test", port=25462,charset='utf8')
            self.cr = self.db.cursor(cursor = pymysql.cursors.DictCursor)
            return True
        except:
            return False

    def get_data_simple(self, query):
        try:
            self.connect_to_database()
            self.cr.execute(query)
        except:
            raise EXECUTE_FAILURE()
            return

        result = self.cr.fetchall()
        return result