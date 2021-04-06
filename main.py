import math
import numpy as np
from gauss_jordan_method import jordan
from utils import file_len

if __name__ == "__main__":
    print("\n\n\n-------------------------------------------\n")
    print("Autorzy: Oskar Kurczewski i Jakub Czarnecki\n")
    print("Metody numeryczne - zadanie 2\n")
    print("Wariant: metoda eliminacji Jordana\n")
    print("-------------------------------------------\n")

    file = open("data.txt", "r")
    number_of_rows = file_len("data.txt")
    spl = file.read().splitlines()

    print("Rows: " + str(number_of_rows))
    print("Content: " + str(spl))
    print("\n\n")

    matrix = []

    for i in range(number_of_rows):
        helper = spl[i].split()
        matrix.append(helper)

    mat = np.asarray(matrix, dtype = np.double)

    print("Macierz:\n" + str(mat))

    jordan(mat)