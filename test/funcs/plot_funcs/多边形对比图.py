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
    plt.rc('legend', fontsize='small')
    matplotlib.rcParams['savefig.dpi'] = 200
    matplotlib.rcParams['font.family']='SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    code=[]
    val=[]
    for i in range(len(datas)):
        code.append(datas[i]['编码'])
        y=[]
        for year in years:
            y.append(datas[i][year])
        val.append(y)
    val=np.array(val)
    
    # # 标准化图
    # val_max = val.max(axis=1).reshape(-1,1)
    # # 处理最大值为0的情况
    # for i in range(len(val_max)):
    #    if val_max[i]==0:
    #        val_max[i]=0.1
    # val /= val_max

    nAttr=len(code)
    angles=np.linspace(0,2*np.pi,nAttr,endpoint=False)

    # 用于绘制闭合环形
    angles=np.concatenate((angles,[angles[0]]))
    code=np.concatenate((code,[code[0]]))
    val=np.concatenate((val,[val[0]]))
    
    fig=plt.figure(facecolor='white')
    plt.subplot(111,polar=True)
    plt.plot(angles,val,'o-',linewidth=1.5,alpha=0.4)
    plt.thetagrids(angles*180/np.pi,code)
    plt.figtext(0.52,0.95,description,ha='center',size=20)
    legend=plt.legend(years,loc=(1,0.80),labelspacing=0.1)
    plt.setp(legend.get_texts(),fontsize='small')
    plt.grid(True)
    plt.savefig('graphs\\%s.png' % description)
