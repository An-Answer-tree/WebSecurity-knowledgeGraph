import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from findiff import FinDiff

threshold_list = [i for i in np.arange(0, 1, 0.05)]

data = np.loadtxt('./result/similarity_matrix_result.csv', delimiter=',')

relations = []
for i in range(0, 2818):
    for j in range(i+1, 2818):
        relations.append(data[i][j])

result_list = []
for i in threshold_list:
    temp = 0
    for j in relations:
        if j >= i:
            temp += 1
    result_list.append(temp / len(relations))

plt.figure()
plt.plot(threshold_list, result_list, color='blue', label='Discrete Points')

interp_func = interp1d(threshold_list, result_list, bounds_error=False)

# 使用 findiff 计算二阶导数
fd = FinDiff(0.05, 2, 2)  # 步长为0.05，计算二阶导数
second_derivatives = fd(interp_func(threshold_list))

print(second_derivatives)

# plt.figure()
# plt.scatter(threshold_list, second_derivatives)
# plt.show()
