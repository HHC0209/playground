import matplotlib.pyplot as plt
import matplotlib
import numpy as np



def plot(datas, years, description):
    '''
    图片需保存在'graphs\\%s.png' % description
    :param datas: 导入文件中包含的数据，是一个字典列表[{'编码':'10020', '地域':'徐州', '级别1':'人口 劳动力', '级别2':'年末户籍户数、人口数',
                                                     '级别3':'总人口', '级别4':'男', '级别5':男, '级别6':'全市', '2010':436.69,
                                                     '2011':431.67, ... '2019':442.74}, {...}, ...]
    :param years: datas中包含的年份, 是一个str列表 ['2010', '2011', ...]
    :param description: 图片名字
    '''
    names = ['%s\n%s' % (data['地域'], data['编码']) for data in datas]  # 横坐标名称
    y_lists = [[0 for i in range(len(datas))] for j in range(len(years))]
    for data_index in range(len(datas)):
        for year_index in range(len(years)):
            y_lists[year_index][data_index] = datas[data_index][years[year_index]]
    bar_width = 70
    x = np.arange(len(names)) * (len(y_lists) * bar_width) * 1.2
    total_count = len(names) * len(y_lists)

    plt.cla()  # 清除之前的绘图数据 必须有
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(total_count * 0.36, 10))
    plt.tight_layout()

    for year_index in range(len(years)):
        if year_index == len(years) // 2:
            plt.bar(x + year_index * bar_width, y_lists[year_index], label=years[year_index], width=bar_width,
                    tick_label=names)
        else:
            plt.bar(x + year_index * bar_width, y_lists[year_index], label=years[year_index], width=bar_width)

        for a, b in zip(x, y_lists[year_index]):
            # 显示在图形上的值
            plt.text(a + year_index * bar_width, b + 0.3, b, ha='center', va='bottom', fontsize=4)

    plt.xticks(x, names, rotation=30, fontsize=10)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8)  # 防止label和图像重合显示不出来
    plt.xlabel('地域 编码')
    plt.ylabel('值')
    plt.rcParams['savefig.dpi'] = 235  # 图片像素
    plt.title(description)
    plt.savefig('graphs\\%s.png' % description)



