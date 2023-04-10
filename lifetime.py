import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class lifetime():
    def __init__(self,filename):
        self.name = filename

    def ReadData(self):
        data_file = os.path.join(fr'.\lifetime\{self.name}.dat')
        data = pd.read_csv(data_file, sep='\s+', header=None)
        # print(len(data[1]))
        return data

    def Figure(self):
        data = self.ReadData()
        one = pd.Series([1 for i in range(1000)])
        plt.figure(dpi=800)
        plt.title(f'{self.name} 1/lifetime')
        plt.style.use('seaborn-whitegrid')
        plt.plot(data[0], data[1],linewidth=2.0)
        # plt.show()
    def savefig(self):
        plt.savefig(fr'.\PNG\{self.name}_lifetime.png', dpi=800)

a1 =lifetime('BP_z')
a1.ReadData()
a1.Figure()
a1.savefig()