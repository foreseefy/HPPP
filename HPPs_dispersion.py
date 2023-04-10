import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mv

class HPPs_dispersion():
    def __init__(self,filename):
        self.name = filename
    def ReadData(self):
        data_file_y = os.path.join(fr'./dispersion/y/n{self.name}.txt')
        data_y = pd.read_csv(data_file_y, sep='\s+', header=None)

        data_file_z = os.path.join(fr'./dispersion/z/n{self.name}.txt')
        data_z = pd.read_csv(data_file_z, sep='\s+', header=None)

        # print(data[0])
        return data_y,data_z

    def Figure(self):
        data_y,data_z = HPPs_dispersion.ReadData(self)
        # print(data_z)
        plt.figure(dpi=200)
        # print(data_y)
        plt.title(f'{self.name}_dispersion')
        # plt.style.use('seaborn-whitegrid')
        plt.scatter(data_y[0], data_y[1],s=3,color='b',label='x-y direction')
        plt.scatter(data_z[0], data_z[1],s=3,color='r',label='z direction')
        #平滑化处理
        # x1_smooth = np.linspace(data_y[0].min(),data_y[0].max())
        # y1_smooth = make_interp_spline(data_y[0],data_y[1],x1_smooth)
        # plt.plot(x1_smooth,y1_smooth)

        #legend
        plt.xlabel('q(1/m)')
        plt.ylabel('frequency(Hz)')
        # Process(target=HPPs_dispersion.Figure(self)).start()
        plt.legend()
        # plt.show()
        # plt.savefig(fr'./PNG/dispersion/{self.name}_dispersion_1e+8.png', dpi=200)
    def savefig(self):
        plt.savefig(fr'./PNG/dispersion/n{self.name}n.png', dpi=500)
        print(fr'{self.name}'+" is saved")

# list = ['BN','BP','AlN','AlP']
list = ['BP','AlN','AlP','BN']
# for item in list:
#     a1 =HPPs_dispersion(item)
#     a1.ReadData()
#     a1.Figure()
#     a1.savefig()
# filename = 'BN'
for item in list:
    # direction = 'z'
    # srcfile_y = f'E:\py_project\Linux_connect\dispersion\bulk\{item}\y\dispersion.txt'
    # dstfile_y = f'E:\py_project\Linux_connect\HPPP_plt\dispersion\y/{item}_bulk.txt'
    # mv.mycopyfile(srcfile_y,dstfile_y)
    # srcfile_z = f'E:\py_project\Linux_connect\dispersion\bulk\{item}\z\dispersion.txt'
    # dstfile_z = f'E:\py_project\Linux_connect\HPPP_plt\dispersion\z\{item}_bulk.txt'
    # mv.mycopyfile(srcfile_z,dstfile_z)

    # plt.figure(dpi=200)
    a1 =HPPs_dispersion(item)
    a1.ReadData()
    a1.Figure()
    a1.savefig()
