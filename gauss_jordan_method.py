import numpy as np

def jordan(matrix):
    rows = matrix.shape[0]
    result = np.zeros(rows, dtype='double')

    for i in range(rows):
        if matrix[i][i] == 0:
            counter = 1
            while (i + counter) < rows and matrix[i + counter][i] == 0:
                counter += 1

            if(i+counter == rows):
                break

            for k in range(rows+1):
                temp = matrix[i][k]
                matrix[i][k] = matrix[i+counter][k]
                matrix[i+counter][k] = temp

        for j in range(rows):
            if i != j:
                ratio = matrix[j][i] / matrix[i][i]

                for k in range(rows + 1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in range(rows):
        if matrix[i][i] == 0 and matrix[i][rows] == 0:
            result = "uklad nieoznaczony"
        elif matrix[i][i] == 0 and matrix[i][rows] != 0:
            result = "uklad sprzeczny"
        else:
            result[i] = matrix[i][rows] / matrix[i][i]
    return result
