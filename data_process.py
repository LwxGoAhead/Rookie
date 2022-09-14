import pandas as pd
from matplotlib.pylab import style
import warnings
warnings.filterwarnings('ignore')
style.use('ggplot')

def train_set_generate(a):
    Data = pd.read_csv(r'D:\G.O.A.T\Ingenuity Cup\面向智能化无线网络规划的网元负荷预测-数据集\train.csv')
    Data = Data.dropna()
    data_old = Data.loc[Data['time'] <= 2022060823]
    data_old['time'] = data_old['time'].astype('str')
    data_old['time'] = pd.to_datetime(data_old['time'], format='%Y%m%d%H')
    table_train = pd.pivot_table(data_old, index=[u'time'], columns=[u'cell'], values=[u'prb'])
    data_train = table_train[table_train.columns[a]]
    index = pd.date_range(start=data_train.index.min(), end=data_train.index.max(), freq='H')
    data_train = data_train.reindex(index)
    train_set = data_train.interpolate(method='linear')
    # plt.plot(data_train.index,data_train.values,label='real')
    # plt.plot(data_fill.index,data_fill.values,label = 'fill',c='r',linestyle = '--')
    # plt.show()

    return train_set
def test_set_generate(a):
    Data = pd.read_csv(r'D:\G.O.A.T\Ingenuity Cup\面向智能化无线网络规划的网元负荷预测-数据集\train.csv')
    Data = Data.dropna()
    data_new = Data.loc[Data['time'] > 2022060823]
    data_new['time'] = data_new['time'].astype('str')
    data_new['time'] = pd.to_datetime(data_new['time'],format='%Y%m%d%H')

    table_true = pd.pivot_table(data_new,index=[u'time'],columns=[u'cell'],values=[u'prb'])
    data_true = table_true[table_true.columns[a]]
    index = pd.date_range(start=data_true.index.min(), end=data_true.index.max(), freq='H')
    data_true = data_true.reindex(index)
    test_set = data_true.interpolate(method='linear')
    return test_set


