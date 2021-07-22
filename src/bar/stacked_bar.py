"""
src: https://blog.csdn.net/m0_45209371/article/details/108241200

"""


#堆叠条形图
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

index = np.arange(4)  
data1 = np.array([1,5,6,3])
data2 = np.array([1,2,1,5])
data3 = np.array([4,8,9,4])

a = 0.3
plt.title('multi bar chart')

plt.bar(index, data1, a, color = 'pink', label = 'a', hatch = '/')
plt.bar(index, data2, a, bottom = data1,           # 堆叠在第一个上方
        color = 'c', label = 'b')
plt.bar(index, data3, a, bottom = (data1 + data2), # 堆叠在第一个和第二个上方
        color = 'orange', alpha = 0.5,label = 'c')

plt.legend()

plt.show()
