import numpy as np

similarity_matrix = np.loadtxt('./result/similarity_matrix_result.csv', delimiter=',')

threshold = 0.85

count = 0
for i in range(2818):
    for j in range(i + 1, 2818):
        if similarity_matrix[i][j] >= threshold:
            similarity_matrix[i][j] = 1
            count += 1
        else:
            similarity_matrix[i][j] = 0
print(count)
np.savetxt('./threshold_decision/0_1_matrix.csv', similarity_matrix, fmt='%d', delimiter=',')




















# import numpy as np
# from matplotlib import pyplot as plt

# threshold_list = [i for i in np.arange(0, 1, 0.05)]

# data = np.loadtxt('./result/similarity_matrix_result.csv', delimiter=',')

# relations = []
# for i in range(0, 2818):
#     for j in range(i+1, 2818):
#         relations.append(data[i][j])

# result_list = []
# for i in threshold_list:
#     temp = 0
#     for j in relations:
#         if j >= i:
#             temp += 1
#     result_list.append(temp / len(relations))

# plt.figure()
# plt.plot(threshold_list, result_list, color='blue', label='Discrete Points')
# plt.xlabel('threshold')
# plt.ylabel('Data proportion')

# # calculate second derivative
# dy_dx = np.gradient(result_list, threshold_list)
# d2y_d2x = np.gradient(dy_dx, threshold_list)

# plt.figure()
# plt.plot(threshold_list, dy_dx)
# plt.xlabel('threshold')
# plt.ylabel('first derivative')

# plt.figure()
# plt.plot(threshold_list, d2y_d2x)
# plt.xlabel('threshold')
# plt.ylabel('second derivative')
# plt.show()
