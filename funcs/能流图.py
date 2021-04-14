import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

# # 示例数据
# datas = [
#     ['外来电', '新能源', '煤炭', '煤炭', '煤炭', '煤炭', '煤炭', '天然气', '天然气', '天然气', '外购焦炭', '石油', '石油', '石油', 'E', 'E', 'E', 'E', 'E',
#      'E', 'C', 'C', 'H', 'H', 'H'],
#     ['E', 'E', 'E', 'C', '规上工业', '规下工业', 'H', 'E', 'H', '第三产业及居民生活', '规上工业', '规上工业', '规下工业', '第三产业及居民生活', '农业', '规上工业',
#      '规下工业', '建筑业', '第三产业及居民生活', '转换损失', '规上工业', '转换损失', '规上工业', '规下工业', '转换损失'],
#     [580.84, 80.69, 2780.76, 504.04, 1478.33, 820.24, 211.01, 498.22, 394.6, 70.9, 726.62, 55.9, 18.59, 992.25, 5.82,
#      1197.5, 292.58, 32.0,
#      392.91, 2020.2, 153.64, 50.4, 408.91, 136.19, 60.57]]
# years = None
# description = "2018苏州 能流图数据"


def plot(datas, years, description):
    '''
    图片需保存在'graphs\\%s.png' % description
    :param datas: 导入文件中包含的数据，是一个字典列表[{'编码':'10020', '地域':'徐州', '级别1':'人口 劳动力', '级别2':'年末户籍户数、人口数',
                                                     '级别3':'总人口', '级别4':'男', '级别5':男, '级别6':'全市', '2010':436.69,
                                                     '2011':431.67, ... '2019':442.74}, {...}, ...]
    :param years: datas中包含的年份, 是一个str列表 ['2010', '2011', ...]
    :param description: 图片名字
    '''
    print(datas)
    print("=" * 16)
    print(years)
    print("=" * 16)
    print(description)
    print("=" * 16)

    plt.cla()  # 清除之前的绘图数据

    cnames = {
        'aliceblue': '#F0F8FF',
        'antiquewhite': '#FAEBD7',
        'aqua': '#00FFFF',
        'aquamarine': '#7FFFD4',
        'azure': '#F0FFFF',
        'beige': '#F5F5DC',
        'bisque': '#FFE4C4',
        'black': '#000000',
        'blanchedalmond': '#FFEBCD',
        'blue': '#0000FF',
        'blueviolet': '#8A2BE2',
        'brown': '#A52A2A',
        'burlywood': '#DEB887',
        'cadetblue': '#5F9EA0',
        'chartreuse': '#7FFF00',
        'chocolate': '#D2691E',
        'coral': '#FF7F50',
        'cornflowerblue': '#6495ED',
        'cornsilk': '#FFF8DC',
        'crimson': '#DC143C',
        'cyan': '#00FFFF',
        'darkblue': '#00008B',
        'darkcyan': '#008B8B',
        'darkgoldenrod': '#B8860B',
        'darkgray': '#A9A9A9',
        'darkgreen': '#006400',
        'darkkhaki': '#BDB76B',
        'darkmagenta': '#8B008B',
        'darkolivegreen': '#556B2F',
        'darkorange': '#FF8C00',
        'darkorchid': '#9932CC',
        'darkred': '#8B0000',
        'darksalmon': '#E9967A',
        'darkseagreen': '#8FBC8F',
        'darkslateblue': '#483D8B',
        'darkslategray': '#2F4F4F',
        'darkturquoise': '#00CED1',
        'darkviolet': '#9400D3',
        'deeppink': '#FF1493',
        'deepskyblue': '#00BFFF',
        'dimgray': '#696969',
        'dodgerblue': '#1E90FF',
        'firebrick': '#B22222',
        'floralwhite': '#FFFAF0',
        'forestgreen': '#228B22',
        'fuchsia': '#FF00FF',
        'gainsboro': '#DCDCDC',
        'ghostwhite': '#F8F8FF',
        'gold': '#FFD700',
        'goldenrod': '#DAA520',
        'gray': '#808080',
        'green': '#008000',
        'greenyellow': '#ADFF2F',
        'honeydew': '#F0FFF0',
        'hotpink': '#FF69B4',
        'indianred': '#CD5C5C',
        'indigo': '#4B0082',
        'ivory': '#FFFFF0',
        'khaki': '#F0E68C',
        'lavender': '#E6E6FA',
        'lavenderblush': '#FFF0F5',
        'lawngreen': '#7CFC00',
        'lemonchiffon': '#FFFACD',
        'lightblue': '#ADD8E6',
        'lightcoral': '#F08080',
        'lightcyan': '#E0FFFF',
        'lightgoldenrodyellow': '#FAFAD2',
        'lightgreen': '#90EE90',
        'lightgray': '#D3D3D3',
        'lightpink': '#FFB6C1',
        'lightsalmon': '#FFA07A',
        'lightseagreen': '#20B2AA',
        'lightskyblue': '#87CEFA',
        'lightslategray': '#778899',
        'lightsteelblue': '#B0C4DE',
        'lightyellow': '#FFFFE0',
        'lime': '#00FF00',
        'limegreen': '#32CD32',
        'linen': '#FAF0E6',
        'magenta': '#FF00FF',
        'maroon': '#800000',
        'mediumaquamarine': '#66CDAA',
        'mediumblue': '#0000CD',
        'mediumorchid': '#BA55D3',
        'mediumpurple': '#9370DB',
        'mediumseagreen': '#3CB371',
        'mediumslateblue': '#7B68EE',
        'mediumspringgreen': '#00FA9A',
        'mediumturquoise': '#48D1CC',
        'mediumvioletred': '#C71585',
        'midnightblue': '#191970',
        'mintcream': '#F5FFFA',
        'mistyrose': '#FFE4E1',
        'moccasin': '#FFE4B5',
        'navajowhite': '#FFDEAD',
        'navy': '#000080',
        'oldlace': '#FDF5E6',
        'olive': '#808000',
        'olivedrab': '#6B8E23',
        'orange': '#FFA500',
        'orangered': '#FF4500',
        'orchid': '#DA70D6',
        'palegoldenrod': '#EEE8AA',
        'palegreen': '#98FB98',
        'paleturquoise': '#AFEEEE',
        'palevioletred': '#DB7093',
        'papayawhip': '#FFEFD5',
        'peachpuff': '#FFDAB9',
        'peru': '#CD853F',
        'pink': '#FFC0CB',
        'plum': '#DDA0DD',
        'powderblue': '#B0E0E6',
        'purple': '#800080',
        'red': '#FF0000',
        'rosybrown': '#BC8F8F',
        'royalblue': '#4169E1',
        'saddlebrown': '#8B4513',
        'salmon': '#FA8072',
        'sandybrown': '#FAA460',
        'seagreen': '#2E8B57',
        'seashell': '#FFF5EE',
        'sienna': '#A0522D',
        'silver': '#C0C0C0',
        'skyblue': '#87CEEB',
        'slateblue': '#6A5ACD',
        'slategray': '#708090',
        'snow': '#FFFAFA',
        'springgreen': '#00FF7F',
        'steelblue': '#4682B4',
        'tan': '#D2B48C',
        'teal': '#008080',
        'thistle': '#D8BFD8',
        'tomato': '#FF6347',
        'turquoise': '#40E0D0',
        'violet': '#EE82EE',
        'wheat': '#F5DEB3',
        'white': '#FFFFFF',
        'whitesmoke': '#F5F5F5',
        'yellow': '#FFFF00',
        'yellowgreen': '#9ACD32'
    }
    color_lst = list(cnames.values())
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

    label = new_label


    source = [all_names.index(val) for val in datas[0]]
    print(type(source))
    target = [all_names.index(val) for val in datas[1]]
    value = [val for val in datas[2]]

    import plotly.graph_objects as go

    node_color = color_lst[3: 3 + len(label)]
    link_color = [node_color[node] for node in source]
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=15,
            line=dict(color="black", width=0.5),
            label=label,
            color=node_color,
        ),
        link=dict(
            source=source,  # indices correspond to labels, eg A1, A2, A2, B1, ...
            target=target,
            value=value,
            color=link_color

        ))])

    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    fig.show()
    
    # import plotly.io as pio
    # pio.orca.config.executable = '/path/to/pyinstalled/orca/orca.exe'
    # fig.write_image('graphs\\%s.png' % description) # conda install -c plotly plotly-orca