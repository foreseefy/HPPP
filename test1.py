import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import epsilion_figure

#玻恩有效电荷
# OUTCAR_filename = input('OUTCAR_filename')
# Born_data_file = os.path.join(fr'C:\Users\ADMIN\Desktop\data_analyse\OUTCAR\OUTCAR_{epsilion_figure.file_name}.txt')
# txt = pd.read_table(Born_data_file,sep='\s+',skiprows=8,names=['num','xx','yy','zz'])
# print(txt)
# frequency_window = epsilion_figure.bar()
# # print(frequency_window)
# cha =  txt.loc[1,'yy'] - txt.loc[2,'zz']
# pinjun = (txt.loc[1,'yy'] + txt.loc[2,'zz'])/2
# print(pinjun)
# print(txt.loc[1,'yy'],txt.loc[2,'zz'])
plt.style.use('ggplot')
#BN
x1 = [2.16315,2.16315]
x1_2 = [1.623,1.623]
y1,y1_2= [2.323, 2.419],[4.023, 4.698]
plt.plot(x1,y1,color='r',linewidth=3.0,label = 'BN')
plt.plot(x1,y1_2,color='r',linewidth=3.0)

#AlN
x2 = [0.63,0.63]
x2_2 = [2.83,2.83]
y2,y2_2 = [1.809, 1.921],[2.664, 2.84]
plt.plot(x2,y2,color='b',linewidth=3.0,label = 'AlN')
plt.plot(x2,y2_2,color='b',linewidth=3.0)

#BP
x3 = [0.0026,0.0026]
x3_2 =[0.51,0.51]
y3 = [2.361, 2.401]
plt.plot(x3,y3,color='g',linewidth=3.0,label = 'BP')

#AlP
x4 = [0.16,0.16]
x4_2 = [2.27,2.27]
y4,y4_2 = [1.255, 1.275],[1.436, 1.436]
plt.plot(x4,y4,color='black',label = 'AlP',linewidth=3.0)
plt.plot(x4,y4_2,color='black',linewidth=3.0)

plt.ylabel('frequency/1.0e+13')
plt.xlabel('Absolute value of difference between Zz and Z⊥')

# if len(frequency_window) < 4 :
#     y1 = [frequency_window[0],frequency_window[1]]
# else:
#     y1 = [frequency_window[0],frequency_window[1]]
#     y2 = [frequency_window[2],frequency_window[3]]
# x1 = [cha,cha]
# plt.plot(x1,y1,color='r')
# if y2:
#     plt.plot(x1, y2, color='r')
plt.legend(loc=0,ncol=2)
plt.show()

