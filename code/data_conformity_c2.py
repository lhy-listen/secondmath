# 本文件用于将格式化的数据整理

import pandas as pd
import numpy as np

## 读取 data_reduction_c2.py 中的数据

item_list = np.load('./data/item_list.npy', allow_pickle=True)
item_list = item_list.tolist()
class_list = np.load('./data/class_list.npy', allow_pickle=True)
class_list = class_list.tolist()
class_dict = np.load('./data/class_dict.npy', allow_pickle=True)

#print(item_list)
#print(type(item_list))
## 从C2中读取数据

data_c2 = pd.read_csv('./data/C2_1_0.csv')
#print (data_c2.head(),'\n',data_c2.tail())

## 按单品和类整理数据
###  ----------------------day0---------------------------  index0 日期
### |code0              |code1|code2|code3|code4|code5|...| index1 单品编码索引
### |volume|volume*price|.................................| index2 0：编码；1：销量；2：销售额
###  ----------------------day1---------------------------
### .......................................................

###  -----------------------------------------------------
###  ----------------------day0---------------------------
### |class0             |class1|class2|class3|class4|.....|
### |volume|volume*price|.................................|
###  ----------------------day1---------------------------
### .......................................................

### 按单品整理数据
data_item = []
for day in range(0,1095):
    data_c2_day = data_c2[data_c2['date'].astype(int) == day]
    data_item_day = []
    for code in item_list:
        volume = []
        volume.append(code)
        volume.append(data_c2_day[data_c2_day['code']==code].iloc[:,2].sum())
        volume.append((data_c2_day[data_c2_day['code']==code].iloc[:,3]*data_c2_day[data_c2_day['code']==code].iloc[:,2]).sum())
        data_item_day.append(volume)
        print('condition:',day,code,'item')
    data_item.append(data_item_day)
np.save('./data/data_item.npy',data_item)
### 按类整理数据
data_class = []
for day in range(0,1095):
    data_c2_day = data_c2[data_c2['date'].astype(int) == day]
    data_class_day = []
    for cls in class_list:    
        volume = []
        volume.append(cls)
        volume.append(data_c2_day[data_c2_day['class']==cls].iloc[:,2].sum())
        volume.append((data_c2_day[data_c2_day['class']==cls].iloc[:,3]*data_c2_day[data_c2_day['class']==cls].iloc[:,2]).sum())
        data_class_day.append(volume)
        print('condition:',day,cls,'class')
    data_class.append(data_class_day)
np.save('./data/data_class.npy',data_class)