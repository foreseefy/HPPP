import yaml
import numpy as np
import re

with open('./band.yaml') as f:
    content = yaml.load(f,Loader=yaml.FullLoader)

patten = re.compile('q-position')
n1 = patten.findall(str(content))

def load_data():
    q_list = []
    fre_list = []
    dict = {}
    for i in range(len(n1)):
        q_position = content['phonon'][i]['q-position']
        q_list.append(q_position)
        frequency = content['phonon'][i]['band']
        fre_list.append(frequency)

        # dict.update({i:frequency})

    return q_list,fre_list

def data_analyse():
    q_list,fre_list = load_data()
    q_vector = np.array(q_list).reshape(102,3)
    Acoustic = []
    LO = []
    TO = []



print(load_data())
# data_analyse()



# print(content['phonon'][0]['band'][1]['eigenvector'])