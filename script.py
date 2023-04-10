import numpy as np

# 从txt文件中读取数据
data = np.loadtxt('./others/BN_n.txt')

# 获取x和y值
x = data[:, 0]
y = data[:, 1]

# 计算新的x值和y值
new_x = []
new_y = []

for i in range(len(x) - 1):
    new_x.append(x[i])
    new_x.append((x[i] + x[i+1]) / 2)
    new_y.append(y[i])
    new_y.append((y[i] + y[i+1]) / 2)

new_x.append(x[-1])
new_y.append(y[-1])

# 线性插值
interp_func = np.interp(new_x, x, y)

# 将新数据写入txt文件
with open('./others/BN_n_n.txt', 'w') as f:
    for i in range(len(new_x)):
        f.write(f"{new_x[i]} {interp_func[i]}\n")
