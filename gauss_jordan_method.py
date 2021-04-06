import sys
import numpy as np

def gauss_jordan_method(matrix):
    number_of_columns = matrix.shape[1]
    result = np.zeros(number_of_columns, dtype='double')

    for i in range(number_of_columns):
        if matrix[i][i] == 0.0:
            sys.exit('dzielenie przez 0')

        for j in range(number_of_columns):
            if i != j:
                ratio = matrix[j][i] / matrix[i][i]

                for k in range(number_of_columns + 1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in range(number_of_columns):
        result[i] = matrix[i][number_of_columns] / matrix[i][i]
    print(str(matrix))
    print(str(result))

    return result
