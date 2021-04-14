from scipy.optimize import curve_fit
import numpy as np


def CFfunc(x, A, B, C, D, E):
    return A * x ** 4 + B * x ** 3 + C * x ** 2 + D * x + E


def forecast(years, y_arrays, predict_years):
    '''
    函数名必须为forecast!!!
    :param x: np.array([0,1,2,3,4...])
    :param y: np.array([[1,2,3,4,5...], [2,3,4,5,6...], ...])
    :return: 预测值列表
    '''
    years = [int(year) for year in years]
    predict_years = [int(pyear) for pyear in predict_years]
    x_array = np.array([year - min(years) for year in years]) # 使temp从0开始 作为预测函数的x数据列表
    temp = []
    for y_array in y_arrays:
        x_array_copy = x_array.copy()
        y_pred = []
        try:
            popt, _ = curve_fit(CFfunc, x_array, y_array, maxfev=50000)
            for year in range(max(years)+1, max(predict_years) + 1):
                x = year - min(years)
                y_pred.append(CFfunc(x, popt[0], popt[1], popt[2], popt[3], popt[4]))
        except:
            y_pred = [float('nan')] * (max(predict_years) - max(years))
        temp.append(y_pred)
    return temp
