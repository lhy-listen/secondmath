# 本文件用于将C2数据集的每日单次销售数据进行格式化
import numpy as np
import pandas as pd

## 从C1中读取单品和类别数据

data_c1 = pd.read_csv('./data/C1.csv')
print(data_c1.head())
item_list = data_c1['code'].drop_duplicates()
class_list = data_c1['class'].drop_duplicates()
np.save('./data/item_list.npy',item_list)
np.save('./data/class_list.npy',class_list)

### 把类别信息储存为字典格式

class_dict = {data_c1.iloc[i,0]:data_c1.iloc[i,2] for i in range(len(data_c1))}
print(dict)
np.save('./data/class_dict.npy',class_dict)

## 从C2中读取数据

data_c2 = pd.read_csv('./data/C2.csv')
print(data_c2.head())
### 格式化日期
data_c2['date'] = pd.to_datetime(data_c2['date'])
data_c2['date'] = data_c2['date'] - data_c2.iloc[0,0]
data_c2['date'] = data_c2['date'].apply(lambda x: x.days)
print(data_c2.head(),'\n',data_c2.tail())
### 去除销售时间数据
data_c2 = data_c2.drop('time',axis=1)
print(data_c2.head(),'\n',data_c2.tail())
### 增加类别信息
data_c2['class'] = data_c2['code'].map(class_dict)
data_c2.to_csv('./data/C2_1_0.csv',index=False)
print(data_c2.head(),'\n',data_c2.tail())

