import math
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mv
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# 介电函数类，两个bool分别是实部和虚部介电函数的显示
class JieDianHanShu():
    def __init__(self, FileName, bool1, bool2):
        self.name = FileName
        self.Re = bool1
        self.Im = bool2

    def ReadData(self):
        data_file = os.path.join(fr'./dielectric/%s.txt'
                                 % self.name)
        data = pd.read_table(data_file, sep='\s+', header=None,
                             names=['w', 'q', 'k', 'ε_xx', 'ε2', 'ε3', 'ε_yy', 'ε5', 'ε_zz',
                                    'Imε_xx', 'ε8', 'ε9', 'Imε_yy',
                                    'ε11', 'Imε_zz'])
        x = np.array([[data['w']], [data['ε_xx']], [data['ε_yy']], [data['ε_zz']],
                      [data['Imε_xx']], [data['Imε_yy']], [data['Imε_zz']]])
        return x

    def lab(self):
        data_file = os.path.join('./dielectric/BN_lab.txt')
        data = pd.read_table(data_file, sep='\s+', header=None,
                             names=['f', 'ε'])
        x= np.array(data['f'])*29979245800*1.0e-12
        y= np.array(data['ε'])

        return x,y
    def sim(self):
        data_yfile = os.path.join('./dielectric/sim_y.txt')
        data_y = pd.read_table(data_yfile, sep='\s+', header=None,
                             names=['f', 'ε'])
        x1 = np.array(data_y['f'])*29979245800*1.0e-12
        y1 = np.array(data_y['ε'])

        data_zfile = os.path.join('./dielectric/sim_z.txt')
        data_z = pd.read_table(data_zfile, sep='\s+', header=None,
                               names=['f', 'ε'])
        x2 = np.array(data_z['f'])*29979245800*1.0e-12
        y2 = np.array(data_z['ε'])
        return x1,y1,x2,y2

    def JiedianHanShuTu(self):
        # 主图
        plt.figure(dpi=800)
        plt.style.use('seaborn-whitegrid')

        # m, n = JieDianHanShu.lab(self)
        # # print([m[0],m[26]], [n[0],n[26]],color='b')
        # #
        # plt.scatter(m[0:26],n[0:26] ,color='r',s=4)
        # plt.scatter(m[27:59], n[27:59],color='r',s=4)
        # 实部
        # x1,y1,x2,y2 = JieDianHanShu.sim(self)
        # plt.scatter(x1,y1,color='r',s=2,label="cal")
        # plt.scatter(x2,y2,color='r',s=2)
        global xr
        xr = JieDianHanShu.ReadData(self)[0][0] * 1.0e-12
        if self.Re:
            plt.plot(xr, JieDianHanShu.ReadData(self)[1][0],
                     linewidth=2.0, label='Re ε$_{x}$',color="b")
            plt.plot(xr, JieDianHanShu.ReadData(self)[2][0],
                     linewidth=2.0, label='Re ε$_{y}$',color="b")
            plt.plot(xr, JieDianHanShu.ReadData(self)[3][0],
                     linewidth=2.0, label='Re ε$_{z}$',color="g")
        # 虚部
        if self.Im:
            plt.plot(xr, JieDianHanShu.ReadData(self)[4][0],
                     linewidth=1.0, label='Im ε$_{x}$',color="b", linestyle='--')
            plt.plot(xr, JieDianHanShu.ReadData(self)[5][0],
                     linewidth=1.0, label='Im ε$_{y}$', color="b",linestyle='--')
            plt.plot(xr, JieDianHanShu.ReadData(self)[6][0],
                     linewidth=1.0, label='Im ε$_{z}$', color="g",linestyle='--')



    def Width(self):
       # 双曲频段
        JieDianChengJi = [JieDianHanShu.ReadData(self)[1][0] * JieDianHanShu.ReadData(self)[3][0]]
        # print(JieDianHanShu.ReadData()[1][0])
        # print(JieDianChengJi[0].tolist())
        Neww = JieDianHanShu.ReadData(self)[0][0]
        # print(Neww)
        NewChengJi = JieDianChengJi[0].tolist()
        alist1 = []
        for i in range(len(Neww)):
            if NewChengJi[i] <= 0:
                alist1.append(Neww[i])
        def FourNums(list):
            alist = []
            alist.append(list[0])
            for i in range(len(list)):
                if list[i] - list[i - 1] > 0.1e+13:
                    alist.append(list[i - 1])
                    alist.append(list[i])
            alist.append(list[-1])
            return alist

        FourNumber = FourNums(alist1)
        return FourNumber

    def XiuShi(self,Width):
         FourNumber = JieDianHanShu.Width(self)
         # FourNumber = [23.23,24.19,40.23,46.98]
         # FourNumber = [18.09,19.21,26.64,28.40]
         # FourNumber = [12.55,12.75]
         print(FourNumber)
         x_min = 0.8*FourNumber[0]                     #AlN_z(0.45)
         x_max = 2.05*FourNumber[0]                     #AlN_z(4.7)
         x = np.linspace(x_min,x_max)



         # plt.xlim(1.15e1,1.2e1)
         # plt.xlim(3.22e1,3.27e1)

         y_min = 1.5*min(JieDianHanShu.ReadData(self)[1][0].min(),
                     JieDianHanShu.ReadData(self)[2][0].min(),
                     JieDianHanShu.ReadData(self)[3][0].min())
         y_max = 1.0*max(JieDianHanShu.ReadData(self)[1][0].max(),
                     JieDianHanShu.ReadData(self)[2][0].max(),
                     JieDianHanShu.ReadData(self)[3][0].max())


         # m,n = JieDianHanShu.lab(self)


         # print(FourNumber[0]-0.1e+13,y_max/6)
         if Width :
             if len(FourNumber) > 2:
                 plt.text(FourNumber[0]*1.0e-12,y_max/15,r'$TO$',fontdict={'size':'7','color':'b'})
                 plt.text(FourNumber[1]*1.0e-12,y_max/15,r'$LO$',fontdict={'size':'7','color':'b'})
                 plt.text(FourNumber[2]*1.0e-12,y_max/15,r'$TO$',fontdict={'size':'7','color':'b'})
                 plt.text(FourNumber[3]*1.0e-12,y_max/15,r'$LO$',fontdict={'size':'7','color':'b'})

                 plt.axvline(FourNumber[0]*1.0e-12, color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvline(FourNumber[1]*1.0e-12, color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvspan(FourNumber[0]*1.0e-12,FourNumber[1]*1.0e-12,color='gray',lw='2',alpha=0.4)
                 plt.axvline(FourNumber[2]*1.0e-12, color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvline(FourNumber[3]*1.0e-12, color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvspan(FourNumber[2]*1.0e-12, FourNumber[3]*1.0e-12, color='gray', lw='2', alpha=0.4)

             else:
                 plt.text(FourNumber[0]*1.0e-12, y_max / 6, r'$TO$', fontdict={'size': '5', 'color': 'b'})
                 plt.text(FourNumber[1]*1.0e-12, y_max / 6, r'$LO$', fontdict={'size': '5', 'color': 'b'})
                 plt.axvline(FourNumber[0]*1.0e-12, color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvline(FourNumber[1]*1.0e-12, color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvspan(FourNumber[0]*1.0e-12,FourNumber[1]*1.0e-12,color='gray',lw='2',alpha=0.4)


     # 其他修饰


         plt.xlim(23,25)
         plt.ylim(-50,50 )
         plt.xlabel('frequency(THz)')

         plt.ylabel('Real permittivity')
         plt.title(f'{self.name}')
         plt.legend()

         # plt.show()

    def save(self):

        plt.savefig(fr'./PNG/dielectric/{self.name}.png',dpi=800)
        # plt.show()
def main(filename):


    # srcfile = f'/public2/home/fangy/Program/dielectric/{item}/dielectric.txt'
    # dstfile = f'/public2/home/fangy/Program/HPPP_plt/dielectric/{item}.txt'
    # mv.mycopyfile(srcfile,dstfile)
    a1 =JieDianHanShu(filename,1,1)
    a1.JiedianHanShuTu()
    a1.XiuShi(1)
    a1.save()

main()