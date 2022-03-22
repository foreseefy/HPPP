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
        data_file = os.path.join(fr'.\dielectric\%s.txt'
                                 % self.name)
        data = pd.read_table(data_file, sep='\s+', header=None,
                             names=['w', 'q', 'k', 'ε_xx', 'ε2', 'ε3', 'ε_yy', 'ε5', 'ε_zz',
                                    'Imε_xx', 'ε8', 'ε9', 'Imε_yy',
                                    'ε11', 'Imε_zz'])
        x = np.array([[data['w']], [data['ε_xx']], [data['ε_yy']], [data['ε_zz']],
                      [data['Imε_xx']], [data['Imε_yy']], [data['Imε_zz']]])
        return x

    def JiedianHanShuTu(self):
        # 主图
        plt.figure(dpi=800)
        plt.style.use('seaborn-whitegrid')
        # 实部
        if self.Re:
            plt.plot(JieDianHanShu.ReadData(self)[0][0], JieDianHanShu.ReadData(self)[1][0],
                     linewidth=2.0, label='Reε_xx')
            plt.plot(JieDianHanShu.ReadData(self)[0][0], JieDianHanShu.ReadData(self)[2][0],
                     linewidth=2.0, label='Reε_yy')
            plt.plot(JieDianHanShu.ReadData(self)[0][0], JieDianHanShu.ReadData(self)[3][0],
                     linewidth=2.0, label='Reε_zz')
        # 虚部
        if self.Im:
            plt.plot(JieDianHanShu.ReadData(self)[0][0], JieDianHanShu.ReadData(self)[4][0],
                     linewidth=1.0, label='Imε_xx', linestyle='--')
            plt.plot(JieDianHanShu.ReadData(self)[0][0], JieDianHanShu.ReadData(self)[5][0],
                     linewidth=1.0, label='Imε_yy', linestyle='--')
            plt.plot(JieDianHanShu.ReadData(self)[0][0], JieDianHanShu.ReadData(self)[6][0],
                     linewidth=1.0, label='Imε_zz', linestyle='--')

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
            if NewChengJi[i] < 0:
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

        # print(FourNums)
    def XiuShi(self,Width):
         FourNumber = JieDianHanShu.Width(self)
         # print(FourNumber)
         x_min = FourNumber[0] - 1.0e+13
         x_max = FourNumber[0] + 2.6e+13

         plt.xlim(x_min,x_max)
         y_min = min(JieDianHanShu.ReadData(self)[1][0].min(),
                     JieDianHanShu.ReadData(self)[2][0].min(),
                     JieDianHanShu.ReadData(self)[3][0].min())
         y_max = max(JieDianHanShu.ReadData(self)[1][0].max(),
                     JieDianHanShu.ReadData(self)[2][0].max(),
                     JieDianHanShu.ReadData(self)[3][0].max())
         plt.ylim(y_min / 5, y_max / 5 )
         # print(FourNumber[0]-0.1e+13,y_max/6)
         if Width :
             if len(FourNumber) > 2:
                 plt.text(FourNumber[0],y_max/6,r'$TO$',fontdict={'size':'7','color':'b'})
                 plt.text(FourNumber[1],y_max/6,r'$LO$',fontdict={'size':'7','color':'b'})
                 plt.text(FourNumber[2],y_max/6,r'$TO$',fontdict={'size':'7','color':'b'})
                 plt.text(FourNumber[3],y_max/6,r'$LO$',fontdict={'size':'7','color':'b'})

                 plt.axvline(FourNumber[0], color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvline(FourNumber[1], color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvspan(FourNumber[0],FourNumber[1],color='gray',lw='2',alpha=0.4)
                 plt.axvline(FourNumber[2], color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvline(FourNumber[3], color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvspan(FourNumber[2], FourNumber[3], color='gray', lw='2', alpha=0.4)

             else:
                 plt.text(FourNumber[0], y_max / 6, r'$TO$', fontdict={'size': '5', 'color': 'b'})
                 plt.text(FourNumber[1], y_max / 6, r'$LO$', fontdict={'size': '5', 'color': 'b'})
                 plt.axvline(FourNumber[0], color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvline(FourNumber[1], color='gray', linewidth=1.0, linestyle='-.')
                 plt.axvspan(FourNumber[0],FourNumber[1],color='gray',lw='2',alpha=0.4)


     # 其他修饰


         plt.xlabel('frequency')
         plt.ylabel('Real permittivity')
         plt.title(f'{self.name}')
         plt.legend()

         # plt.show()


    def save(self):

        plt.savefig(fr'.\PNG\dielectric_{self.name}_graph.png',dpi=800)
        # plt.show()


# a1 = JieDianHanShu('AlP', 1, 1)
# a1.JiedianHanShuTu()
# a1.XiuShi(1)
# a1.save()

# filename = 'BAs'
# graph_name = 'dielectric'
# mv.rename(filename,graph_name)
# a1 =JieDianHanShu(filename,1,1)
# a1.JiedianHanShuTu()
# a1.XiuShi(1)
# a1.save()

