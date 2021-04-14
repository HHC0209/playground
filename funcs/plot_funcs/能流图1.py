from pyecharts import options as opts
from pyecharts.charts import Sankey, Grid
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot
import win32api
import os
from PyQt5.QtWidgets import QMessageBox

def plot(datas, years, description):
    '''
    图片需保存在'graphs\\%s.png' % description
    :param datas: 导入文件中包含的数据，是一个字典列表[{'编码':'10020', '地域':'徐州', '级别1':'人口 劳动力', '级别2':'年末户籍户数、人口数',
                                                     '级别3':'总人口', '级别4':'男', '级别5':男, '级别6':'全市', '2010':436.69,
                                                     '2011':431.67, ... '2019':442.74}, {...}, ...]
    :param years: datas中包含的年份, 是一个str列表 ['2010', '2011', ...]
    :param description: 图片名字
    '''
    # print(datas)
    # print("=" * 16)
    # print(years)
    # print("=" * 16)
    # print(description)
    # print("=" * 16)

    plt.cla()  # 清除之前的绘图数据

    all_names = list(set.union(set(datas[1]), set(datas[0])))
    label = all_names
    # print("\n\nAll names")
    # print(all_names)
    import collections
    d = collections.defaultdict(float)
    n = len(datas[0])
    sources_name = datas[0]
    target_name = datas[1]
    source_name_set = set(datas[0])
    target_names_set = set(datas[1])
    # print(source_name_set)
    # print('\n\n')
    # print(target_names_set)

    target_only_names = target_names_set.difference(source_name_set)
    values = datas[2]
    for i in range(n):
        name = sources_name[i]
        val = values[i]
        d[name] += val
    for i in range(n):
        name = target_name[i]
        if name in target_only_names:
            d[name] += values[i]
    new_label = []
    for name in all_names:
        new_label.append(name + " " + str(round(d[name],2)))

    # label = new_label


    source = [all_names.index(val) for val in datas[0]]
    print(type(source))
    target = [all_names.index(val) for val in datas[1]]
    value = [val for val in datas[2]]


    node = []
    for item in all_names:
        dic = {'name' : item}
        node.append(dic)

    link = []
    for i in range(len(source)):
        dic = {'source' : all_names[source[i]], 'target' : all_names[target[i]], 'value' : value[i]}
        link.append(dic)

    print(node)
    print('\n\n')
    print(link)
    pic = (
    Sankey(init_opts = opts.InitOpts(width = '1200px', height = '800px')).add("",
         node,
         link,
         linestyle_opt=opts.LineStyleOpts(opacity = 0.3, curve = 0.5, color = 'source'),
         label_opts=opts.LabelOpts(position = 'right'),
         node_gap = 30,#节点之间的距离,(查看垂直图片的操作orient="vertical")
         pos_top = '10%'
    ).set_global_opts(title_opts=opts.TitleOpts(title = 'Basic Sankey Diagram'))
)
    
    # grid = Grid()
    # grid.add(pic, grid_opts = opts.GridOpts(pos_top = '30%'))

    # win32api.ShellExecute(0, 'open', '../../', '', '', 1)
    save_path = os.getcwd() + '/graphs/test.html'
    pic.render(path = save_path)
    # make_snapshot(snapshot,"*.html","*.png")
    # pic.show()
    print("能流图1绘制完成！")
    return save_path
    # messageBox = QMessageBox(QMessageBox.information, "提示", "能流图已绘制完成并保存在路径\"%s\"下" % save_path, QMessageBox.Yes, QMessageBox.No)
    # Qyes = messageBox.addButton(self.tr("设置"), QMessageBox.YesRole)
    # Qno = messageBox.addButton(self.tr("忽略"), QMessageBox.NoRole)


    # import plotly.graph_objects as go

    # node_color = color_lst[3: 3 + len(label)]
    # link_color = [node_color[node] for node in source]
    # fig = go.Figure(data=[go.Sankey(
    #     node=dict(
    #         pad=15,
    #         thickness=15,
    #         line=dict(color="black", width=0.5),
    #         label=label,
    #         color=node_color,
    #     ),
    #     link=dict(
    #         source=source,  # indices correspond to labels, eg A1, A2, A2, B1, ...
    #         target=target,
    #         value=value,
    #         color=link_color

    #     ))])

    # fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    # fig.show()
    
    # import plotly.io as pio
    # pio.orca.config.executable = '/path/to/pyinstalled/orca/orca.exe'
    # fig.write_image('graphs\\%s.png' % description) # conda install -c plotly plotly-orca

