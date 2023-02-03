# 행렬에서 최댓값을 찾는다.
# 행렬을 입력 받늗다.
# 행에서 최대값을 찾는다.
def find_max(matrix):
    max_value_matrix = 0
    for i in range(9):
        max_value_row = max(matrix[i])
        if max_value_row > max_value_matrix:
            max_value_matrix = max_value_row
            max_value_matrix_index = [i, matrix[i].index(max_value_matrix)]

    max_value_matrix_index[0] += 1
    max_value_matrix_index[1] += 1
    return max_value_matrix, max_value_matrix_index


max_value, index = find_max(matrix=[list(map(int, input().split())) for i in range(9)])

print(max_value)
print(index[0], end=' ')
print(index[1])



