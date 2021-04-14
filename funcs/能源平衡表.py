import numpy as np
import numpy
import pandas as pd
import sympy


def belowconsumeELE(da89,da97,da85,da86,da87,da88,da90):
    arrayele=np.zeros(5,dtype=int)
    da93=da97/da89*da85
    da94=da97/da89*da86
    da95=da97/da89*da87
    da96 = da97 / da89 * da88
    da98 = da97 / da89 * da90
    return da93,da94,da95,da96,da98


def analyze(datapure):
    for yr in range(2008,2090):
        if str(yr) in datapure[0].keys():
            year=yr
            break
    year=str(year)

    datas={}
    for dataselect in datapure:
        try:
            dataselect[year] = float(dataselect[year])
        except:
            dataselect[year] = 0
        datas[dataselect['编码']]=dataselect

    data9=datas['250030'][year]
    data10=datas['250040'][year]
    data11=datas['250020'][year]
    data12=datas['250010'][year]
    totalkwhoutput = datas['45040'][year]
    data17=datas['57380'][year]*0.000122835033-totalkwhoutput*1.22835033  # 前是万千瓦时，后是亿千瓦时
    data66=(datas['51170'][year]*0.7143+datas['51500'][year]*0.9+datas['51830'][year]*0.6142)/10000  # 原煤、洗精煤、煤制品
    data82=datas['57390'][year]*0.000122835033
    data89=datas['50440'][year]*0.000122835033
    data97=datas['57400'][year]*0.000122835033-data89
    data103=datas['57590'][year]*0.000122835033
    data110=(datas['57600'][year]+datas['57610'][year]+datas['57620'][year])*0.000122835033
    data118=datas['57630'][year]*0.000122835033
    elethecoal=(datas['51360'][year]*0.7143+datas['51690'][year]*0.9+datas['52020'][year]*0.6142)/10000
    elethegas=(datas['53340'][year]*1.4286+datas['53670'][year]*1.4714+datas['54000'][year]*1.4714+datas['54330'][year]*1.4571+datas['54660'][year]*1.4286+datas['54990'][year]*1.7143)/10000  # 原油、汽油、煤油、柴油、燃料油、液化石油气
    data30=elethegas # 在无锡模式中，认定石油都用来发电，而没有用来供热
    data44=0
    eletheng=(datas['52680'][year]*0.001214+datas['53010'][year]*0.000166814286)
    data34=datas['55320'][year]/293076 # 无锡模式中，认定热能在电力、热力供应业中的应用只有发电
    data13=(datas['50450'][year]*0.1843+datas['50460'][year])/10000
    data85=(datas['50250'][year]*0.7143+datas['50260'][year]*0.9+datas['50270'][year]*0.6142)/10000-data66-elethecoal
    data86=(datas['50330'][year]*1.4286+datas['50340'][year]*1.4714+datas['50350'][year]*1.4714+datas['50360'][year]*1.4571+datas['50370'][year]*1.4286+datas['50380'][year]*1.7143)/10000-elethegas
    data87=datas['50310'][year]*0.001214+datas['50320'][year]*0.000166814286-eletheng
    data88=datas['50280'][year]*0.00009714
    data90=datas['50430'][year]/293076-data34
    data91=0
    data92=6.89079
    data93,data94,data95,data96,data98=belowconsumeELE(data89,data97,data85,data86,data87,data88,data90)
    data18=0 # 外来热能供应
    data116=datas['320040'][year]
    data108=datas['320030'][year]-data116
    data119=0
    data111=0
    cokingcoal=datas['300010'][year]+datas['300020'][year]+datas['300030'][year]
    cokingoutcok=datas['300040'][year]
    cokingoutother=datas['300050'][year]+datas['300060'][year]
    coalcoktrans=cokingoutcok/cokingcoal
    coalothertrans=cokingoutother/cokingcoal
    coallosstrans=1-coalcoktrans-coalothertrans
    data67=data66*coalcoktrans
    data68=data66*coalothertrans
    data69=data66*coallosstrans
    provinceagricoalconsume=datas['300070'][year]+datas['300080'][year]+datas['300090'][year]  #省农业用煤
    provinceagrigasconsume=datas['300100'][year]+datas['300110'][year]+datas['300120'][year]+datas['300130'][year]+datas['300140'][year]+datas['300150'][year]
    provinceagrimachinepower=datas['300570'][year]  #省农机动力值
    urbanagrimachinepower=datas['20660'][year]
    data78=provinceagricoalconsume*urbanagrimachinepower/provinceagrimachinepower
    data79=provinceagrigasconsume*urbanagrimachinepower/provinceagrimachinepower
    provinceconstructcoalconsume=datas['300160'][year]+datas['300170'][year]+datas['300180'][year]
    provinceconstructgasconsume=datas['300190'][year]+datas['300200'][year]+datas['300210'][year]+datas['300220'][year]+datas['300230'][year]+datas['300240'][year]
    provinceconstructoutput=datas['300580'][year]
    urbanconstructoutput=datas['60020'][year]
    data99=provinceconstructcoalconsume*urbanconstructoutput/provinceconstructoutput
    data100=provinceconstructgasconsume*urbanconstructoutput/provinceconstructoutput
    provincetertiarycoalconsume=datas['300250'][year]+datas['300260'][year]+datas['300270'][year]+datas['300330'][year]+datas['300340'][year]+datas['300350'][year]+datas['300410'][year]+datas['300420'][year]+datas['300430'][year]
    provinceresidentcoalconsume=datas['300490'][year]+datas['300500'][year]+datas['300510'][year]
    provincepermanentpopulation=datas['300590'][year]
    urbanpermanentpopulation=datas['10030'][year]
    data106=provincetertiarycoalconsume*urbanpermanentpopulation/provincepermanentpopulation
    data114=provinceresidentcoalconsume*urbanpermanentpopulation/provincepermanentpopulation
    provincetertiarygasconsume=datas['300280'][year]+datas['300290'][year]+datas['300300'][year]+datas['300310'][year]+datas['300320'][year]+datas['300360'][year]+datas['300370'][year]+datas['300380'][year]+datas['300390'][year]+datas['300400'][year]+datas['300440'][year]+datas['300450'][year]+datas['300460'][year]+datas['300470'][year]+datas['300480'][year]
    provinceresidentgasconsume=datas['320020'][year]+datas['300520'][year]+datas['300530'][year]+datas['300540'][year]+datas['300550'][year]+datas['300560'][year]
    provincevehiclenum=datas['300600'][year]
    urbanvehiclenum=datas['70230'][year]
    urbantertiarylpgconsume=datas['320010'][year]-datas['320020'][year]
    urbanresidentlpgconsume=datas['320020'][year]
    data107=provincetertiarygasconsume*urbanvehiclenum/provincevehiclenum+urbantertiarylpgconsume
    data115=provinceresidentgasconsume*urbanvehiclenum/provincevehiclenum+urbanresidentlpgconsume
    # a1 = 0.41  把a1和x1都搞成未知的
    # x1 = 464.0411
    q = 0.7#0.7只是暂编的 # 燃煤发电量占总火力发电量的比例，要来自数据库
    a2 = 0.47 # 油电转换
    c2 = data30
    a3 = 0.78
    c6 = 0
    c5 = data34  # 热能去发电
    # a5 = 0.86*a1
    c4 = data13
    x4 = c4*0.78  # c4、x4存在垃圾发电、供热比例，3.5
    E = totalkwhoutput-data9-data10-data11-data12
    data40=E
    p1 = 0.871
    c1 = elethecoal
    p3 = 0.9
    c3 = eletheng
    c7 = 0
    p5 = 0.86 * p1
    # a4 = a1/p1
    T = data90+data98+data111+data119-data18
    data55=T
    a1, a4, a5, x1, x3 = sympy.symbols("a1 a4 a5 x1 x3")
    a = sympy.solve(
        [a5 - 0.86 * a1, a4 - a1 / p1, a1 * x1 - E * q, a1 * x1 + a2 * c2 + a3 * (x3 + c6) + a4 * c5 + a5 * x4 - E,
         p1 * (c1 - x1) + p3 * (c3 - x3 + c7) + p5 * (c4 - x4) - T], [a1, a4, a5, x1, x3])
    turea=a[1]
    for i in range(2):
        if a[1][i]<0:
            turea=a[0]
            break
    a1=turea[0]
    a4=turea[1]
    data29=turea[3]
    data31=turea[4]
    data14=turea[2]*x4
    data15=p5*(c4-x4)
    data16=data13-data14-data15
    data36=0
    data50=0
    data41=data29+data30+data31+data34+data36-data40
    data43=elethecoal-data29
    data45=eletheng-data31
    data56=data43+data44+data45+data50-data55
    for i in [9,10,11,12,13,14,15,16,17,18,29,30,31,34,36,40,41,43,44,45,50,55,56,66,67,68,69,78,79,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,106,107,108,110,111,114,115,116,118,119]:
        designation='data'+str(i)
        if eval(designation)<0:
            exec('data'+str(i)+'=0')
    data1=data29+data43+data66+data78+data85+data93+data99+data106+data114
    data2=data30+data44+data79+data86+data94+data100+data107+data115
    data3=data31+data45+data87+data95+data108+data116
    data4=data88+data96-data67
    data7=data13+data91
    data8=data36+data50+data92-data68
    dataarray=np.array([
        (data1,data2,data3,data4,' ',' ',data7,data8),
        (' ',' ',' ',' ',data9,' ',' ',' '),
        (' ',' ',' ',' ',data10,' ',' ',' '),
        (' ',' ',' ',' ',data11,' ',' ',' '),
        (' ',' ',' ',' ',data12,' ',' ',' '),
        (' ',' ',' ',' ',' ',' ',data13,' '),
        (' ',' ',' ',' ',data14,data15,' ',' '),
        (' ',' ',' ',' ',' ',data16,' ',' '),
        (' ',' ',' ',' ',data17,' ',' ',' '),
        (' ',' ',' ',' ',' ',data18,' ',' '),
        (data29,data30,data31,' ',' ',data34,' ',data36),
        (' ',' ',' ',' ',data40,' ',' ',' '),
        (' ',' ',' ',' ',data41,' ',' ',' '),
        (data43,data44,data45,' ',' ',' ',' ',data50),
        (' ',' ',' ',' ',' ',data55,' ',' '),
        (' ',' ',' ',' ',' ',data56,' ',' '),
        (data66,' ',' ',' ',' ',' ',' ',' '),
        (' ',' ',' ',data67,' ',' ',' ',data68),
        (' ',' ',' ',data69,' ',' ',' ',' '),
        (data78,data79,' ',' ',data82,' ',' ',' '),
        (data85,data86,data87,data88,data89,data90,data91,data92),
        (data93,data94,data95,data96,data97,data98,' ',' '),
        (data99,data100,' ',' ',data103,' ',' ',' '),
        (data106,data107,data108,' ',data110,data111,' ',' '),
        (data114,data115,data116,' ',data118,data119,' ',' ')
    ])
    print(dataarray)
    # return datatable
    header_v = ['1、供本地消费量(+)','2、水力发电量(+)','3、核能发电量(+)','4、太阳能发电量(+)','5、风力发电量(+)','6、焚烧垃圾热电联产的消耗(-)','7、焚烧垃圾热电联产的产出(+)','8、焚烧垃圾热电联产的转换损失量(-)','9、外来电能供应量(+)','10、外来热能供应量(+)','11、电能生产（除去水力和新能源）的消耗(-)','12、电能生产（除去水力和新能源）的产出(+)','13、电能生产（除去水力和新能源）的转换损失量(-)','14、热能生产的消耗(-)','15、热能生产的产出(+)','16、热能生产的转换损失量(-)','17、炼焦过程的消耗(-)','18、炼焦过程的产出(+)','19、炼焦过程的转换损失量(-)','20、农业终端消费量(-)','21、规上工业终端消费量(-)','22、规下工业终端消费量(-)','23、建筑业终端消费量(-)','24、第三产业终端消费量(-)','25、居民生活终端消费量(-)']
    header_h = ['煤炭','石油','天然气','焦炭','电能','热能','生活垃圾和生物质废料用于燃料','其它焦化产品']
    return dataarray, [header_h, header_v]
