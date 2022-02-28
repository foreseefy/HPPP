import os
import pandas as pd
import matplotlib.pyplot as plt
import JiedianHanshu

class BornCharge():
    def __init__(self,filename):
        self.name = filename

    def ReadData(self):
        Born_data_file = os.path.join(
            fr'.\OUTCAR\OUTCAR_{self.name}.txt')
        a2 = JiedianHanshu.JieDianHanShu(self.name,1,1)
        Width = a2.Width()
        if len(Width) >2:
            y = [Width[0],Width[1],Width[2],Width[3]]
        else:
            y = [Width[0],Width[1]]
        # y = [Width[0],Width[1]]
        txt = pd.read_table(Born_data_file, sep='\s+', skiprows=8, names=['num', 'xx', 'yy', 'zz'])
        BornCharges =[txt.loc[0,'xx'],txt.loc[1,'yy'],txt.loc[2,'zz']]
        x = [abs(-txt.loc[2,'zz'] + txt.loc[0,'xx']),abs(-txt.loc[2,'zz'] + txt.loc[0,'xx'])]
        list = [x,y]

        return list


plt.figure()
plt.style.use('ggplot')


# list = ['BN','BP','AlN','AlP','GaP']
def HuaTu(list):
    for i in range(len(list)):
        data = BornCharge(list[i]).ReadData()

        color = ['blue','red','green','black','gray']
        if len(data[1]) == 4:
            plt.plot(data[0], [data[1][0],data[1][1]], color = color[i],label=list[i],linewidth=3.0)
            plt.plot(data[0], [data[1][2],data[1][3]], color = color[i],linewidth=3.0)
        else:
            plt.plot(data[0], [data[1][0],data[1][1]], color = color[i],label=list[i],linewidth=3.0)
        # plt.plot(data[0], data[1][0], color='r', linewidth=3.0, label=self.name)
        # plt.plot(data[0], data[1][1], color='r', linewidth=3.0, label=self.name)
        # plt.legend(
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.legend()
    plt.ylabel('frequency（1.0e+13）')
    plt.xlabel('Absolute value of difference between Z⊥ and Z∥（e）')

    # plt.show()
    plt.savefig(f'.\PNG\BornCharge.png', dpi=800)

list = ['BN','BP','AlN','AlP','GaP']
HuaTu(list)