import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mv

class HPPs_dispersion():
    def __init__(self,filename):
        self.name = filename

    def ReadData(self):
        data_file = os.path.join(fr'.\dispersion\{self.name}.txt')
        data = pd.read_csv(data_file, sep='\s+', header=None)
        # print(data[0])
        return data

    def Figure(self):
        data = self.ReadData()
        plt.figure(dpi=200)
        plt.title(f'{self.name}_dispersion')
        plt.style.use('seaborn-whitegrid')
        plt.scatter(data[0], data[1],s=3)
        plt.xlabel('q(1/m)')
        plt.ylabel('frequency(Hz)')
        # plt.legend()
        # plt.show()
    def savefig(self):
        plt.savefig(fr'.\PNG\{self.name}_dispersion.png', dpi=200)
list = ['BN','BP2','AlN','AlP','GaP']
for item in list:
    a1 =HPPs_dispersion(item)
    a1.ReadData()
    a1.Figure()
    a1.savefig()
# filename = 'BN'
# newfilename = filename + '2'
# mv.rename(filename)
# a1 =HPPs_dispersion(newfilename)
# a1.ReadData()
# a1.Figure()
# a1.savefig()
