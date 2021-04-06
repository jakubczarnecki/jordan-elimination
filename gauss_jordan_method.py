import sys
import numpy as np

def jordan(matrix):

    rows = matrix.shape[0]
    result = np.zeros(rows, dtype='double')

    for i in range(rows):
        if matrix[i][i] == 0.0:
            sys.exit('dzielenie przez 0')
        for j in range(rows):
            if i != j:
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(rows + 1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    for i in range(rows):
        result[i] = matrix[i][rows] / matrix[i][i]

    # print(str(matrix))
    print("\n\nWynik: " + str(result))

    return result