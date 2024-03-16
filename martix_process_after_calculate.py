import numpy as np

with open('similarity_scores.txt', 'r') as file:
    data = eval(file.read())

result_matrix = np.zeros((2818, 2818))
for i in range(2818):
    result_matrix[i][i:2818] = data[i]

np.savetxt('similarity_matrix_result.csv', result_matrix, fmt='%f')
