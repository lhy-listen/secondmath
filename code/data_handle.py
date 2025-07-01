import numpy as np

# data = np.load('./data/data_item.npy', allow_pickle=True)
# data = data.tolist()
# print('this is the first day',data[0])
# print('this is the last day',data[1])

data_class = np.load('./data/data_class.npy', allow_pickle=True)
data_class = data_class.tolist()
print('this is the first day',data_class[0])
print('this is the last day',data_class[1])