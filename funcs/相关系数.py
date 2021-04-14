import numpy as np

def is_number(str):
    try:
        # 因为使用float有一个例外是'NaN'
        if str=='NaN':
            return False
        float(str)
        return True
    except ValueError:
        return False

def analyze(datas):
    # 筛选传入年份
    years = []
    for key in datas[0].keys():
        if is_number(key):
            years.append(key)
    # print(years)
    # 生成输入到分析函数中数组
    values = []
    for i in range(len(datas)):
        temp = np.array([])
        for year in years:
            if datas[i][year] == None:
                temp = np.append(temp, 0)
            else:
                temp = np.append(temp, float(datas[i][year]))
        values.append(temp)
    values = np.array(values)
    return np.corrcoef(values), None
