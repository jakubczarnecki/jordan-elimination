import math
import numpy as np
import gauss_jordan_method
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

    wspolczynniki = []
    wektor = []

    for i in range(number_of_rows):
        if (i % 2 == 0):
            helper = spl[i].split()
            wspolczynniki.append(helper)
        else:
            wektor.append(spl[i])

    wsp = np.asarray(wspolczynniki, dtype = np.double)
    wek = np.asarray(wektor, dtype = np.double)

    print("Wspolczynniki:\n" + str(wsp))
    print("Wektor:\n" + str(wek))
    print("\n\n")



