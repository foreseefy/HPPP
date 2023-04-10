import os
import pandas as pd
import numpy as np

def ExchangeData(direction):
    data_file = os.path.join('D:\Apostgraduate\Program\dispersion\QPOINTS\QPOINTS_y_n.txt')
    data = pd.read_table(data_file, sep='\s+', skiprows=1, names=[ 'x', 'y', 'z'])
    if direction == 'y':
        data = data.loc[:,['z','x','y']]
    elif direction == 'z':
        data = data.loc[:,['z','y','x']]
    elif direction == 'x':
        data = data.loc[:,['x','y','z']]
    # print(data)
    endfile_path = f'D:\Apostgraduate\Program\dispersion\QPOINTS\QPOINTS_{direction}_n.txt'
    data.to_csv(endfile_path, index=False, header=False, sep="\t")
    with open(endfile_path, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('599\n' + content)

ExchangeData('z')


