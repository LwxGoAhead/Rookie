import numpy as np
from statsmodels.graphics.gofplots import qqplot
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller as ADF
import itertools
import matplotlib.pyplot as plt
from matplotlib.pylab import style
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import pacf
import statsmodels.tsa.stattools as st
from dateutil.relativedelta import relativedelta
from datetime import datetime
import data_process
from sklearn import preprocessing
import warnings
warnings.filterwarnings('ignore')
style.use('ggplot')



train_set = data_process.train_set_generate(1)
# mm = preprocessing.MinMaxScaler()
# train_set = mm.fit_transform(train_set.reshape(-1,1))
test_set = data_process.test_set_generate(1)

####画出原始数据的时序图
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.figure()
# plt.title("网元prb效率时序图")
# plt.xticks(rotation=90)
# plt.xlabel('时间')
# plt.ylabel('网元prb效率')
# plt.grid(True)
# plt.plot(train_set.index, train_set, 'k-')
# plt.show()
#

#ADF检验
print('原始数据的ADF检验结果为：', ADF(train_set)) #平稳性检测
#白噪声检验
print('原始数据的白噪声检验结果为：', acorr_ljungbox(train_set, lags=1))
order_analyze = st.arma_order_select_ic(train_set, max_ar=5, max_ma=5, ic=['aic', 'bic'])
print('AIC准则选出的最优参数为',order_analyze.aic_min_order)
print('bIC准则选出的最优参数为',order_analyze.bic_min_order)

#数据归一化



# 画acf和pacf图像
# def show_acf(data):
#     acf = plot_acf(data,lags=40)
#     plt.title("ACF")
#     acf.show()
#     pacf = plot_pacf(data,lags=40,method='ywm')
#     plt.title("PACF")
#     pacf.show()
# show_acf(train_set)
# pacf_x, interval = pacf(x = train_set, nlags=40, alpha=0.05)
# print('原始序列的PACF:\n',pacf_x)
# print('PACF95%置信区间下界:\n',interval[:,0]-pacf_x)
# print('PACF95%置信区间上界:\n',interval[:,1]-pacf_x)
"""
完全符合平稳序列的特征
"""
#fit model
start_date = train_set.index.max()+relativedelta(hours=1)
end_date = start_date + relativedelta(hours=47)
model = ARIMA(train_set,order=(order_analyze.bic_min_order[0],0,order_analyze.bic_min_order[1]),freq='H')
model_fit = model.fit()
predict_data = model_fit.predict(start=start_date,end=end_date)
#predict_data = model_fit.predict()
print(model_fit.summary())





#####模型的平均绝对百分比误差(越小越好,最佳值为0)
# def MAPE(Y_real,Y_pre):#计算mape
#     from sklearn.metrics import mean_absolute_percentage_error
#     return mean_absolute_percentage_error(Y_real,Y_pre)
# error = MAPE(test_set.values,predict_data.values)
# print('预测值与实际值的平均绝对百分比误差为:\n',error)



# D-W检验残差序列
# resid = model_fit.resid#残差
# fig = plt.figure(figsize=(12,8))
# ax = fig.add_subplot(111)
# fig = qqplot(resid, line='q', ax=ax, fit=True)

# 画出对比图
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.figure()
# plt.title("预测与实际")
# plt.xticks(rotation=90)
# plt.xlabel('time')
# plt.ylabel('网元负荷')
# plt.grid(True)
# plt.plot(predict_data.index, predict_data, 'k-',label = '预测数据')
# plt.plot(test_set.index, test_set, 'g-',label = '实际数据')  # 画出拟合曲线
# plt.show()

# for i in table.columns:
#     table[i] = table[i].dropna()
#     index = pd.date_range(start=table[i].index.min(), end=table[i].index.max(), freq='H')
#     table[i].reindex(index)
#     # ADFres = ADF(table[i])
#     #print(ADFres)
#     model = ARIMA(table[i], order=(0, 0, 48),freq='H')
#     model_fit = model.fit()
#     predict_data = model_fit.forecast(48)
#     print(predict_data)
#     quit()

#table.to_csv(r'D:\G.O.A.T\Ingenuity Cup\面向智能化无线网络规划的网元负荷预测-数据集\test.csv')
#print(type(Data['time'].values[0]))
