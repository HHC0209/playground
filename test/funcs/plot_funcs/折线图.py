import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

def plot(datas, years, description):
    '''
    图片需保存在'graphs\\%s.png' % description
    :param datas: 导入文件中包含的数据，是一个字典列表[{'编码':'10020', '地域':'徐州', '级别1':'人口 劳动力', '级别2':'年末户籍户数、人口数',
                                                     '级别3':'总人口', '级别4':'男', '级别5':男, '级别6':'全市', '2010':436.69,
                                                     '2011':431.67, ... '2019':442.74}, {...}, ...]
    :param years: datas中包含的年份, 是一个str列表 ['2010', '2011', ...]
    :param description: 图片名字
    '''
    plt.cla()  # 清除之前的绘图数据 必须有
    plt.figure()

    matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
    plt.rc('legend', fontsize='small')
    matplotlib.rcParams['savefig.dpi'] = 200
    # 去除"（预测）"的字符串
    x = range(int(years[0][:4]), int(years[-1][:4])+1)
    code = []
    for i in range(len(datas)):
        code.append(datas[i]['编码'])
        y = []
        for year in years:
            y.append(datas[i][year])
        plt.plot(x,np.array(y),marker='*',ms=10)
        for j in range(len(x)):
            plt.text(x[j], y[j]+0.6, y[j], ha='center', va='bottom', fontsize=7)
        
    plt.legend(code ,loc='upper right',bbox_to_anchor=(1,1),ncol=4,fancybox=True)
    plt.legend:[{}]
    plt.xlabel('年份')
    plt.ylabel('值')
    plt.xticks(x)
    plt.title(description)
    plt.savefig('graphs\\%s.png' % description)
