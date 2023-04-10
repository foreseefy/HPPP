import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_file_o = os.path.join(fr'./others/fw.txt')
data_file = pd.read_table(data_file_o, sep='\s+',names=['w','re','im'])

plt.figure(dpi=200)
plt.plot(data_file['w'], data_file['re'])

plt.xlabel('q')
plt.ylabel('fw')

plt.savefig(fr'./PNG/fw.png', dpi=200)