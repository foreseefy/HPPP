import os
import pandas as pd
import matplotlib.pyplot as plt

import mv

class HPPs_dispersion():
    def __init__(self,filename):
        self.name = filename
    def ReadData(self):
        data_file_y = os.path.join(fr'.\dispersion\y\{self.name}.txt')
        data_y = pd.read_csv(data_file_y, sep='\s+', header=None)

        data_file_z = os.path.join(fr'.\dispersion\z\{self.name}.txt')
        data_z = pd.read_csv(data_file_z, sep='\s+', header=None)

        # print(data[0])
        return data_y,data_z

    def Figure(self):
        data_y,data_z = HPPs_dispersion.ReadData(self)
        plt.figure(dpi=200)
        # print(data_y)
        plt.title(f'{self.name}_dispersion')
        plt.style.use('seaborn-whitegrid')
        plt.scatter(data_y[0], data_y[1],s=1,color='b',label='x-y direction')
        plt.scatter(data_z[0], data_z[1],s=1,color='r',label='z direction')
        plt.xlabel('q(1/m)')
        plt.ylabel('frequency(Hz)')
        # Process(target=HPPs_dispersion.Figure(self)).start()
        plt.legend()
        plt.show()
    def savefig(self):
        plt.savefig(fr'.\PNG\dispersion\{self.name}_dispersion_.png', dpi=200)
# list = ['BN','BP2','AlN','AlP','GaP']
# for item in list:
#     a1 =HPPs_dispersion(item)
#     a1.ReadData()
#     a1.Figure()
#     a1.savefig()
filename = 'BN'
direction = 'y'
srcfile = f'..\dispersion\{filename}\y\dispersion.txt'
dstfile = f'.\dispersion\{direction}\{filename}.txt'
mv.mycopyfile(srcfile,dstfile)
# plt.figure(dpi=200)


a1 =HPPs_dispersion(filename)
a1.ReadData()
a1.Figure()
# a1.savefig()
